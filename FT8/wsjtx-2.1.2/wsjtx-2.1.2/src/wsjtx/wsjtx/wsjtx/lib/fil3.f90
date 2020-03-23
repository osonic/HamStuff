subroutine fil3(x1,n1,c2,n2)

! FIR real-to-complex filter designed using ScopeFIR
!
!-----------------------------------------------
! fsample    (Hz)  12000      Input sample rate
! Ntaps            113        Number of filter taps
! fc         (Hz)  500        Cutoff frequency
! fstop      (Hz)  750        Lower limit of stopband
! Ripple     (dB)  0.2        Ripple in passband
! Stop Atten (dB)  50         Stopband attenuation
! fmix       (HZ)  1500       Mixing frequency
! fout       (Hz)  1500       Output sample rate

! Resulting passband is 1000 - 2000 Hz

! Suggest calling with n1 = 8*n2 + 105, where n2 is the desired number
! of 1500 Hz output samples.

  parameter (NTAPS=113)
  parameter (NH=NTAPS/2)
  parameter (NDOWN=8)                !Downsample ratio = 1/8
  real x1(n1)
  complex z
  complex c2(n1/NDOWN)

! Filter coefficients:
  complex ca(-NH:NH)
  data ca/                                   &
        (-0.001818142144, 0.000000000000),   &
        (-0.000664066641,-0.000664066640),   &
        (-0.000000000000,-0.001044063550),   &
        ( 0.000737290018,-0.000737290010),   &
        ( 0.000908957610,-0.000000000000),   &
        ( 0.000444156615, 0.000444156610),   &
        (-0.000000000000, 0.000202701460),   &
        ( 0.000244876473,-0.000244876470),   &
        ( 0.000978154552, 0.000000000000),   &
        ( 0.001155650277, 0.001155650270),   &
        ( 0.000000000000, 0.002243121590),   &
        (-0.001927618608, 0.001927618600),   &
        (-0.003006201675, 0.000000000000),   &
        (-0.002134087852,-0.002134087850),   &
        ( 0.000000000000,-0.002717699570),   &
        ( 0.001478946738,-0.001478946730),   &
        ( 0.001162489032, 0.000000000000),   &
        (-0.000005589545,-0.000005589540),   &
        (-0.000000000000,-0.001321554800),   &
        ( 0.001873767954,-0.001873767950),   &
        ( 0.003843608784,-0.000000000000),   &
        ( 0.003356874940, 0.003356874940),   &
        (-0.000000000000, 0.005218967040),   &
        (-0.003640348011, 0.003640348010),   &
        (-0.004470167307, 0.000000000000),   &
        (-0.002247131477,-0.002247131470),   &
        (-0.000000000000,-0.001335998900),   &
        (-0.000647656208, 0.000647656200),   &
        (-0.003386100636, 0.000000000000),   &
        (-0.004114456189,-0.004114456180),   &
        ( 0.000000000000,-0.007939147960),   &
        ( 0.006692816134,-0.006692816130),   &
        ( 0.010145641899, 0.000000000000),   &
        ( 0.006920770724, 0.006920770720),   &
        ( 0.000000000000, 0.008285915750),   &
        (-0.003992321524, 0.003992321520),   &
        (-0.001995842303, 0.000000000000),   &
        ( 0.001704388774, 0.001704388770),   &
        (-0.000000000000, 0.007202515550),   &
        (-0.008426458377, 0.008426458370),   &
        (-0.016028350845, 0.000000000000),   &
        (-0.013430355885,-0.013430355880),   &
        (-0.000000000000,-0.020297455950),   &
        ( 0.013791263729,-0.013791263720),   &
        ( 0.016298136197,-0.000000000000),   &
        ( 0.007443596155, 0.007443596150),   &
        (-0.000000000000, 0.002223837360),   &
        ( 0.005924356866,-0.005924356860),   &
        ( 0.020854478160, 0.000000000000),   &
        ( 0.024471928130, 0.024471928130),   &
        ( 0.000000000000, 0.048909701460),   &
        (-0.044508219241, 0.044508219240),   &
        (-0.075874892030, 0.000000000000),   &
        (-0.061450241075,-0.061450241070),   &
        ( 0.000000000000,-0.095332017640),   &
        ( 0.071148679982,-0.071148679980),   &
        ( 0.102420526192, 0.000000000000),   &
        ( 0.071148679982, 0.071148679980),   &
        ( 0.000000000000, 0.095332017640),   &
        (-0.061450241075, 0.061450241070),   &
        (-0.075874892030, 0.000000000000),   &
        (-0.044508219241,-0.044508219240),   &
        ( 0.000000000000,-0.048909701460),   &
        ( 0.024471928130,-0.024471928130),   &
        ( 0.020854478160, 0.000000000000),   &
        ( 0.005924356866, 0.005924356860),   &
        (-0.000000000000,-0.002223837360),   &
        ( 0.007443596155,-0.007443596150),   &
        ( 0.016298136197,-0.000000000000),   &
        ( 0.013791263729, 0.013791263720),   &
        (-0.000000000000, 0.020297455950),   &
        (-0.013430355885, 0.013430355880),   &
        (-0.016028350845, 0.000000000000),   &
        (-0.008426458377,-0.008426458370),   &
        (-0.000000000000,-0.007202515550),   &
        ( 0.001704388774,-0.001704388770),   &
        (-0.001995842303, 0.000000000000),   &
        (-0.003992321524,-0.003992321520),   &
        ( 0.000000000000,-0.008285915750),   &
        ( 0.006920770724,-0.006920770720),   &
        ( 0.010145641899, 0.000000000000),   &
        ( 0.006692816134, 0.006692816130),   &
        ( 0.000000000000, 0.007939147960),   &
        (-0.004114456189, 0.004114456180),   &
        (-0.003386100636, 0.000000000000),   &
        (-0.000647656208,-0.000647656200),   &
        (-0.000000000000, 0.001335998900),   &
        (-0.002247131477, 0.002247131470),   &
        (-0.004470167307, 0.000000000000),   &
        (-0.003640348011,-0.003640348010),   &
        (-0.000000000000,-0.005218967040),   &
        ( 0.003356874940,-0.003356874940),   &
        ( 0.003843608784,-0.000000000000),   &
        ( 0.001873767954, 0.001873767950),   &
        (-0.000000000000, 0.001321554800),   &
        (-0.000005589545, 0.000005589540),   &
        ( 0.001162489032, 0.000000000000),   &
        ( 0.001478946738, 0.001478946730),   &
        ( 0.000000000000, 0.002717699570),   &
        (-0.002134087852, 0.002134087850),   &
        (-0.003006201675, 0.000000000000),   &
        (-0.001927618608,-0.001927618600),   &
        ( 0.000000000000,-0.002243121590),   &
        ( 0.001155650277,-0.001155650270),   &
        ( 0.000978154552, 0.000000000000),   &
        ( 0.000244876473, 0.000244876470),   &
        (-0.000000000000,-0.000202701460),   &
        ( 0.000444156615,-0.000444156610),   &
        ( 0.000908957610,-0.000000000000),   &
        ( 0.000737290018, 0.000737290010),   &
        (-0.000000000000, 0.001044063550),   &
        (-0.000664066641, 0.000664066640),   &
        (-0.001818142144, 0.000000000000)/
  save ca

  n2=(n1-NTAPS+NDOWN)/NDOWN
  k0=NH-NDOWN+1

! Loop over all output samples
  do i=1,n2
     z=0.
     k=k0 + NDOWN*i
     do j=-NH,NH
        z=z + x1(j+k)*ca(j)
     enddo
     c2(i)=z
  enddo

  return
end subroutine fil3
