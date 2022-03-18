# Heart Rate Variability

<p align="justify">Heart Rate Variability describes the oscillation in the time interval between consecutive heartbeats, which can be used as an indicator of the activity of the autonomic nervous system (ANS) and the cardiovascular system (KLEIGER; STEIN; BIGGER, 2005). For this reason, HRV is considered an important tool to provide information about the balance of the sympathetic nervous system (SNS) and the parasympathetic nervous system (PNS).</p>

<p align="justify">According to the definition proposed by Kivikangas, Nacke and Ravaja (2011) Nervous System behavior encompasses three interconnected components: subjective experience, expressive behavior and physiological changes. The physiological changes that occur during a stimulus can be measured through heart rate, galvanic skin response, peripheral temperature, and changes in patterns of brain electrical activity (TOLENTINO et al., 2009). Thayer and Lane's (2000) neurovisceral integration model proposes a reciprocal link between performance of performed functions and physiological processes and suggests HRV as a mediator between physiological and psychological processes (THAYER, LANE, 2000).</p>

<p align="justify">HRV functions as an informative, non-invasive mechanism on health-related cardiovascular parameters. These parameters can be used for clinical purposes, as a marker of stress or for exercise prescription in the fields of medicine, psychology and physical education (RUMENIG et al., 2011). HRV is an indicator of ANS activity that is responsible for numerous control functions in the human body which includes the emotional responses associated with voluntary actions (KOLB, WHISHAW, 2002). The autonomic nervous system regulates the physiological resources of an individual according to the demand required by the environment.</p>

![HRV Time and Frequency Measurements Signal](https://github.com/DiegoPaezA/HRVlibrary/blob/master/hrvanalisis_result.png)

HRV Time and Frequency Measurements Signal



<p align="justify">The most common metrics for the analysis of HRV recognized by the Task Force of the European Society of Cardiology and the North American Society of Pacing Electrophysiology (1996) are presented in Table 1 and Table 2.</p>

<p align="justify">The variables in the time domain are defined as the different statistical parameters that result from the electrocardiographic measurement of the normal RR intervals. These normal RR intervals are statistically and mathematically analyzed to obtain the different parameters. The most commonly used parameters that provide the most information are the following:</p>

### Table 1 variables in the time domain

| Variable | Definition |
| ------------- | ------------- |
|RR [ms]     | Mean RR Range  |
|SDNN [ms]   | Standard deviation of the mean of RR intervals.  |
|rMSSD [ms]  | Square root of the average of squares of the differences between intervals.  |
|NN50        | Number of adjacent RR intervals with duration differences exceeding 50 ms|
|pNN50 [%]| Percentage of adjacent RR intervals with duration differences exceeding 50 ms.|

---------------------------

<p align="justify">Measurement of the frequency spectrum of HRV is commonly obtained using the Fourier Transform, which allows the energy (power) of the RR signal to be decomposed into different frequency components. The spectral components correlate with the different components of the autonomic nervous system. Most of the signal power is in the range 0.003 to 0.4 Hz. The calculated variables are as follows:</p>

### Table 2 variables in the frequency spectrum

 Variable  | Definition |
| ------------- | ------------- |
|TP [ms2] |Total Power. Represents the overall spectrum. It is the variance of all the components of the RR intervals between 0.003 to 0.4 Hz. |
|VLF [ms2]|Very Low Frequency, frequency range from 0.003 to 0.04 Hz. It represents hormonal, vasomotor and thermoregulatory influences. |
|LF [ms2] |Low Frequency, frequency range of 0.04 to 0.15 Hz. Index is related to the level of activation of the SNS. |
|HF [ms2] |High Frequency, frequency range from 0.15 to 0.4 Hz. Ratio is related to the activation level of the PNS. |
|LF/HF    |Ratio between LF and HF. Whose value allows an estimation of the vagal-sympathetic balance. |

<p align="justify">The method used is Welch's Periodogram (1967), which is based on the periodogram method developed by Bartlett (1948). Bartlett's method consists of dividing a sequence of N points into K segments, and then the periodograms of each of the K segments are calculated. The estimate of the Bartlett power spectrum is given by the average of the periodograms of each of the K segments. </p>

## Class Details

<p align="justify">The signal filtering process starts by resampling the VFC signal to a uniformly sampled 1 Hz signal, since as described in section 3.3.2, the recorded VFC signal does not have a constant sampling interval. After resampling, RR intervals that lie outside the upper and lower bounds are discarded, as seen in Figure 36. The limits are calculated from the calculated average of the HRV signal and its interquartile range.</p>

<p align="justify">The frequency analysis of the signal is performed using the Welch periodogram method presented in section 3.4.4. To implement the method, the Scipy Welch library function (SCIPY.ORG, 2013) was used. To calculate the frequency spectrum of the VFC, the signal was prepared by resampling it at a frequency of 4 Hz. With the prepared HRV signal the welch function was applied using a 256-point Hanning window with a 50% overlap and 1024-point FFT.</p>


**References of this work can be found in:** https://repositorio.ufsc.br/handle/123456789/160626 



