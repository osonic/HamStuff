#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import limesdr
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.xlate_filter_taps = xlate_filter_taps = firdes.low_pass(1, 250000, 125000, 25000, firdes.WIN_HAMMING, 6.76)
        self.signal = signal = 1
        self.samp_rate = samp_rate = 200e3
        self.offset = offset = 0
        self.carrier_level = carrier_level = 1
        self.audio_gain = audio_gain = 1

        ##################################################
        # Blocks
        ##################################################
        _signal_sizer = wx.BoxSizer(wx.VERTICAL)
        self._signal_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_signal_sizer,
        	value=self.signal,
        	callback=self.set_signal,
        	label='Signal level',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._signal_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_signal_sizer,
        	value=self.signal,
        	callback=self.set_signal,
        	minimum=0,
        	maximum=2,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_signal_sizer, 6, 3, 1, 1)
        _offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	label='Offset',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_offset_sizer,
        	value=self.offset,
        	callback=self.set_offset,
        	minimum=-25000,
        	maximum=25000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_offset_sizer, 5, 0, 1, 4)
        _carrier_level_sizer = wx.BoxSizer(wx.VERTICAL)
        self._carrier_level_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_carrier_level_sizer,
        	value=self.carrier_level,
        	callback=self.set_carrier_level,
        	label='Carrier level',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._carrier_level_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_carrier_level_sizer,
        	value=self.carrier_level,
        	callback=self.set_carrier_level,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_carrier_level_sizer, 7, 1, 1, 1)
        _audio_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._audio_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_audio_gain_sizer,
        	value=self.audio_gain,
        	callback=self.set_audio_gain,
        	label='Audio gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._audio_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_audio_gain_sizer,
        	value=self.audio_gain,
        	callback=self.set_audio_gain,
        	minimum=0,
        	maximum=2,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_audio_gain_sizer, 6, 1, 1, 1)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_1_0_1_0 = filter.rational_resampler_ccc(
                interpolation=10000,
                decimation=200,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=25,
                decimation=6,
                taps=None,
                fractional_bw=None,
        )
        self.limesdr_sink_0 = limesdr.sink('', 0, '', '')
        self.limesdr_sink_0.set_sample_rate(10e6)
        self.limesdr_sink_0.set_center_freq(7.05e6, 0)
        self.limesdr_sink_0.set_bandwidth(130e6,0)
        self.limesdr_sink_0.set_gain(60,0)
        self.limesdr_sink_0.set_antenna(1,0)
        self.limesdr_sink_0.calibrate(5e6, 0)

        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((signal, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((audio_gain, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.band_pass_filter_0 = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	1, samp_rate, -3000, 3000, 100, firdes.WIN_HAMMING, 6.76))
        self.audio_source_0 = audio.source(48000, '', True)
        self.analog_sig_source_offset_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, offset, carrier_level, 0)
        self.analog_sig_source_offset = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, offset, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_offset, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_offset_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.limesdr_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_1_0_1_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.rational_resampler_xxx_1_0_1_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))

    def get_xlate_filter_taps(self):
        return self.xlate_filter_taps

    def set_xlate_filter_taps(self, xlate_filter_taps):
        self.xlate_filter_taps = xlate_filter_taps

    def get_signal(self):
        return self.signal

    def set_signal(self, signal):
        self.signal = signal
        self._signal_slider.set_value(self.signal)
        self._signal_text_box.set_value(self.signal)
        self.blocks_multiply_const_vxx_0_0.set_k((self.signal, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, -3000, 3000, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_offset_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_offset.set_sampling_freq(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self._offset_slider.set_value(self.offset)
        self._offset_text_box.set_value(self.offset)
        self.analog_sig_source_offset_0.set_frequency(self.offset)
        self.analog_sig_source_offset.set_frequency(self.offset)

    def get_carrier_level(self):
        return self.carrier_level

    def set_carrier_level(self, carrier_level):
        self.carrier_level = carrier_level
        self._carrier_level_slider.set_value(self.carrier_level)
        self._carrier_level_text_box.set_value(self.carrier_level)
        self.analog_sig_source_offset_0.set_amplitude(self.carrier_level)

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        self._audio_gain_slider.set_value(self.audio_gain)
        self._audio_gain_text_box.set_value(self.audio_gain)
        self.blocks_multiply_const_vxx_0.set_k((self.audio_gain, ))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
