# Radix2_16points_FFT
fft16_FullExpand: no loop, fully expand

fft16_FloatPoints: 
  1.  twiddle factor pre calculated
  2.  three-level loop: 
        outer loop: four stages;
        middle loop: how many butterfly computations a stage;
        inner loop: butterfly computation;
  3.  8-bit wide integer input
  4.  float output

fft16_FixedPoint:
  1.  twiddle factor pre calculated
  2.  three-level loop: 
        outer loop: four stages;
        middle loop: how many butterfly computations a stage;
        inner loop: butterfly computation;
  3.  8-bit wide integer input
  4.  Fixed-point output
