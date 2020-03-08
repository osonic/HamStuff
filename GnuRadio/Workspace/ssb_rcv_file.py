#!/usr/bin/env python
#
#                    Weaver SSB demodulation
#
#
#                                          af_loi
#                                            |
#                               --[lpf2i]---(X)---|
#                               |         af_mixi |
#                               |                 |
# signal --[freq xlating]--[split]               (+)----- ssb_demod
#          [fir filter  ]       |                 |  + USB
#                               |         af_mixq |  - LSB
#                               --[lpf2q]---(X)---|
#                                            |
#                                          af_loq
#
#
# Based on code from:
#
#  http://webpages.charter.net/cswiger/weaver.html
#
from gnuradio import gr, blks2
from gnuradio import audio
import sys

class my_graph(gr.top_block):
	def __init__(self, input_filename, tune_freq, bfo_freq, side_band):
		gr.top_block.__init__(self)

    		#sets the rf offset depending on lsb or usb
    		if side_band == 'L' or side_band == 'l':
        		rf_LO = tune_freq - bfo_freq
    		else:
        		rf_LO = tune_freq + bfo_freq

    		#sets the bfo frequency
    		af_LO = bfo_freq


    		rf_sample_rate = 256e3        #data rate of input file
    		fir_decimation = 8
    		af_sample_rate = rf_sample_rate/fir_decimation  #  32kbps

    		
    		#declares the input file to be the signal source
    		src = gr.file_source (gr.sizeof_gr_complex, input_filename)

    		#design a channel filter with 20 KHz cutoff frequency
    		xlate_taps = gr.firdes.low_pass ( 1.0, # gain
						rf_sample_rate,  #input rate
						20e3, #cutoff frequency
						10e3, #transition bandwidth
						gr.firdes.WIN_HAMMING )  #window

		#implement the channel filter and shift the spectrum by rf_LO = tune_freq +/- bfo_freq
    		xlate = gr.freq_xlating_fir_filter_ccf ( fir_decimation, #decimation factor
							xlate_taps, #filter coefficients
							rf_LO, #offset
							rf_sample_rate )  #input rate

    		#separates the real(I) and imag (Q) components
    		split = gr.complex_to_float ()

   		 #create oscillators and the bfo frequency
    		af_loi = gr.sig_source_f (af_sample_rate,gr.GR_COS_WAVE,af_LO,1,0)
    		af_loq = gr.sig_source_f (af_sample_rate,gr.GR_SIN_WAVE,af_LO,1,0)

    		#create and implement LPFs for baseband I and Q (cutoff = 1.8KHz)
    		lpf2_taps = gr.firdes.low_pass ( 1.0, af_sample_rate, 1.8e3, 600, gr.firdes.WIN_HAMMING)
    		lpf2i = gr.fir_filter_fff (1, lpf2_taps)
    		lpf2q = gr.fir_filter_fff (1, lpf2_taps)

    		#multiply I and Q with their respective BFO oscillator
    		af_mixi = gr.multiply_ff ()
    		af_mixq = gr.multiply_ff ()

    		# add or subtract depending on sideband
    		if side_band == 'L' or side_band == 'l':
    		    sum = gr.sub_ff ()
    		else:
    		    sum = gr.add_ff ()

    		#volume .00003 for 50Mhz sigs and .015 for 4192 khz
    		scale = gr.multiply_const_ff(.03)

    		# resampler to convert 32kbps to 48kbps for computer audio card
    		rsamp=blks2.rational_resampler_fff(3,2)


    		out = audio.sink (long(48000))

    		src_sink = gr.file_sink(gr.sizeof_gr_complex,"src.dat")
    		xlate_sink = gr.file_sink(gr.sizeof_gr_complex,"xlate.dat")
    		lpf2i_sink = gr.file_sink(gr.sizeof_float,"lpf2i.dat")
    		afmixi_sink = gr.file_sink(gr.sizeof_float,"afmixi.dat")
    		afmixq_sink = gr.file_sink(gr.sizeof_float,"afmixq.dat")
    		rsamp_sink = gr.file_sink(gr.sizeof_float,"rsamp.dat")


    		self.connect (src, xlate)
    		self.connect (xlate, split)
    		self.connect (xlate, xlate_sink)
    		self.connect (src, src_sink)

    		self.connect ((split, 0), lpf2i)
    		self.connect (lpf2i, (af_mixi, 0))
    		self.connect (lpf2i, lpf2i_sink)

    		self.connect (af_loi, (af_mixi, 1))
    		self.connect (af_mixi, (sum, 0))
    		self.connect (af_mixi, afmixi_sink)


    		self.connect ((split, 1), lpf2q)
    		self.connect (lpf2q, (af_mixq, 0))
    		self.connect (af_loq, (af_mixq, 1))
    		self.connect (af_mixq, (sum, 1))
    		self.connect (af_mixq, afmixq_sink)

    		self.connect (sum, scale)
    		self.connect (scale, rsamp)
    		self.connect (rsamp, out)
    		self.connect (rsamp, rsamp_sink)


def main (args):
    if len(args) != 4:
        sys.stderr.write ('usage: ssb_rcv_file filename freq(Hz) bfo(Hz) sideband{U,L}\n')
        sys.exit (-1)

    fg = my_graph (args[0], float(args[1]), float(args[2]), args[3][0])

    fg.start ()       
    raw_input ('Press Enter to quit: ')
    fg.stop ()

if __name__ == '__main__':
    main (sys.argv[1:])



