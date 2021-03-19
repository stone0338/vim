Vim�UnDo� "���l�vU�T<qC�;OaIN�'i�/�&4ޗ��   8   Hdef detect_alpha(x, sf, thresh=0.25, wlt_params={'nc': 10, 'cf': '10'}):      A      2       2   2   2    `P�    _�                        B    ����                                                                                                                                                                                                                                                                                                                                                             `P�    �          ;      Fdef detect_alpha(x, sf, thresh=0.25, wlt_params={'nc': 12, 'cf': ''}):5�_�                            ����                                                                                                                                                                                                                                                                                                                               !           >       V   C    `P     �                "    if wlt_params['cf'] == 'auto':   J        # Compute the power spectrum and find the peak 11-16 Hz frequency.   M        psd, freqs = psd_array_multitaper(x, sf, fmin=11, fmax=16, verbose=0)   0        wlt_params['cf'] = freqs[np.argmax(psd)]   >        print('Central frequency: %.2f Hz' % wlt_params['cf'])5�_�                            ����                                                                                                                                                                                                                                                                                                                               !          >       V   C    `P     �                 5�_�                       8    ����                                                                                                                                                                                                                                                                                                                               !          >       V   C    `P    �          5      Hdef detect_alpha(x, sf, thresh=0.25, wlt_params={'nc': 12, 'cf': '10'}):5�_�                    %        ����                                                                                                                                                                                                                                                                                                                            %   ,       3   *       V   8    `Pb     �   $   %          -    # Find supra-threshold values and indices   ,    supra_thresh_bool = norm_power >= thresh   5    supra_thresh_idx = np.where(supra_thresh_bool)[0]       ;    # Extract duration, frequency and amplitude of spindles   T    sp = np.split(supra_thresh_idx, np.where(np.diff(supra_thresh_idx) != 1)[0] + 1)   9    idx_start_end = np.array([[k[0], k[-1]] for k in sp])   C    sp_dur = (np.diff(idx_start_end, axis=1) / sf).flatten() * 1000   :    sp_amp, sp_freq = np.zeros(len(sp)), np.zeros(len(sp))       for i in range(len(sp)):   -        sp_amp[i] = np.ptp(detrend(x[sp[i]]))   J        sp_freq[i] = np.median((sf / (2 * np.pi) * np.diff(phase[sp[i]])))       E    sp_params = {'Duration (ms)' : sp_dur, 'Frequency (Hz)': sp_freq,   *                 'Amplitude (uV)': sp_amp}5�_�                    $        ����                                                                                                                                                                                                                                                                                                                            %   ,       %   *       V   8    `Pc     �   #   $           5�_�                    %       ����                                                                                                                                                                                                                                                                                                                            $   ,       $   *       V   8    `Pf     �   $              '    return supra_thresh_bool, sp_params5�_�      	              %       ����                                                                                                                                                                                                                                                                                                                            $   ,       $   *       V   8    `Pi    �   $                  return 5�_�      
           	   "       ����                                                                                                                                                                                                                                                                                                                            $   ,       $   *       V   8    `P�     �   "   $   %    5�_�   	              
   "   	    ����                                                                                                                                                                                                                                                                                                                            %   ,       %   *       V   8    `P�     �   !   #   &      '    power = np.square(np.abs(analytic))5�_�   
                 "       ����                                                                                                                                                                                                                                                                                                                            %   ,       %   *       V   8    `P�     �   "   $   '          �   "   $   &    5�_�                    #       ����                                                                                                                                                                                                                                                                                                                            &   ,       &   *       V   8    `P�     �   "   $   '          power_all = np.square()5�_�                    #   !    ����                                                                                                                                                                                                                                                                                                                            &   ,       &   *       V   8    `P�     �   "   $   '      #    power_all = np.square(np.abs())5�_�                    #   #    ����                                                                                                                                                                                                                                                                                                                            &   ,       &   *       V   8    `P�     �   #   %   (          �   #   %   '    5�_�                    $       ����                                                                                                                                                                                                                                                                                                                            '   ,       '   *       V   8    `P�     �   #   %   (           power_relative = np.divide()5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            '   ,       '   *       V   8    `P�     �   '                  return power5�_�                    $   
    ����                                                                                                                                                                                                                                                                                                                            '   ,       '   *       V   8    `P�     �   #   %   (      6    power_relative = np.divide(power_alpha, power_all)5�_�                    (       ����                                                                                                                                                                                                                                                                                                                            '   ,       '   *       V   8    `P�    �   '                  return power_alpha5�_�                           ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P%     �                    Returns5�_�                           ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P%     �                    -------5�_�                           ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P&     �                *    supra_thresh_bool : 1D-array (boolean)5�_�                           ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P&     �                K        Boolean array indicating for each point if it is a spindles or not.5�_�                           ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P'     �                    sp_params : dict5�_�                           ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P(     �                (        Spindles parameters dictionnary.5�_�                            ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P)    �                 5�_�                           ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `PH     �                D    norm_power = (power - power.min()) / (power.max() - power.min())5�_�                            ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `PI    �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `PT    �                  �               5�_�                    #        ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   #            �   #            5�_�      !              #        ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�    �   "   #           5�_�      "           !   (        ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   (               �   (            5�_�   !   #           "   *        ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   *            �   *            5�_�   "   $           #   *        ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   )   *           5�_�   #   %           $   1        ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   1               �   1            5�_�   $   &           %   2   1    ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   1              2power_alpha, power_alpha_relative = detect_alpha()5�_�   %   '           &   2   6    ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   1              8power_alpha, power_alpha_relative = detect_alpha(data[])5�_�   &   (           '   !   	    ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   !   #   3       �   !   #   2    5�_�   '   )           (   "       ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P�     �   "   %   4       �   "   $   3    5�_�   (   *           )   5   8    ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P
     �   4              9power_alpha, power_alpha_relative = detect_alpha(data[0])5�_�   )   +           *   4       ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P     �   3   6   5      data = raw.get_data()5�_�   *   ,           +   5       ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P     �   4   6   6      sfreq = raw.info[]5�_�   +   -           ,   5       ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P     �   4   6   6      sfreq = raw.info[""]5�_�   ,   .           -   6       ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P     �   6               �   6            5�_�   -   1           .   6   =    ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P!   	 �   5   7   8      >power_alpha, power_alpha_relative = detect_alpha(data[0], sf=)5�_�   .   2   /       1      A    ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P�     �          8      Hdef detect_alpha(x, sf, thresh=0.25, wlt_params={'nc': 10, 'cf': '10'}):5�_�   1               2      C    ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P�    �          8      Gdef detect_alpha(x, sf, thresh=0.25, wlt_params={'nc': 10, 'cf': 10'}):5�_�   .   0       1   /   5       ����                                                                                                                                                                                                                                                                                                                            !           "           V        `P`     �   4   6   8      sfreq = int(raw.info["sfreq"]5�_�   /               0   5       ����                                                                                                                                                                                                                                                                                                                            !           "           V        `Pc     �   4   6   8      sfreq = int(raw.info["sfreq"])5�_�              !       (        ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P�     �   (   )           �   (   *       <       Mdef spindles_detect(x, sf, thresh=0.25, wlt_params={'nc': 12, 'cf': 'auto'}):   <        """Simple spindles detector based on Morlet wavelet.                   Parameters                   ----------                        x : 1D-array   &                            EEG signal   *                                sf : float   :                                        Sampling frequency   :                                            thresh : float   E                                                    Threshold (0 - 1)   I                                                        wlt_params : dict   \                                                                Morlet wavelet parameters ::       i                                                                            'nc' : number of oscillations   |                                                                                    'cf' : central frequency (int or 'auto')       _                                                                                        Returns   c                                                                                            -------   �                                                                                                supra_thresh_bool : 1D-array (boolean)   �                                                                                                        Boolean array indicating for each point if it is a spindles or not.   |                                                                                                            sp_params : dict   �                                                                                                                    Spindles parameters dictionnary.   {                                                                                                                        """   �                                                                                                                            from scipy.signal import detrend   �                                                                                                                                from mne.time_frequency import morlet, psd_array_multitaper       �                                                                                                                                    if wlt_params['cf'] == 'auto':   �                                                                                                                                                # Compute the power spectrum and find the peak 11-16 Hz frequency.   �                                                                                                                                                        psd, freqs = psd_array_multitaper(x, sf, fmin=11, fmax=16, verbose=0)   �                                                                                                                                                                wlt_params['cf'] = freqs[np.argmax(psd)]   �                                                                                                                                                                        print('Central frequency: %.2f Hz' % wlt_params['cf'])       �                                                                                                                                                                            # Compute the wavelet and convolve with data   �                                                                                                                                                                                wlt = morlet(sf, [wlt_params['cf']], n_cycles=wlt_params['nc'])[0]   �                                                                                                                                                                                    analytic = np.convolve(x, wlt, mode='same')   �                                                                                                                                                                                        phase = np.angle(analytic)                                                                                                                                                                                                  # Square and normalize the magnitude from 0 to 1 (using the min and max)   �                                                                                                                                                                                                power = np.square(np.abs(analytic))                                                                                                                                                                                                      norm_power = (power - power.min()) / (power.max() - power.min())       �                                                                                                                                                                                                        # Find supra-threshold values and indices   �                                                                                                                                                                                                            supra_thresh_bool = norm_power >= thresh                                                                                                                                                                                                                  supra_thresh_idx = np.where(supra_thresh_bool)[0]                                                                                                                                                                                                                          # Extract duration, frequency and amplitude of spindles  (                                                                                                                                                                                                                        sp = np.split(supra_thresh_idx, np.where(np.diff(supra_thresh_idx) != 1)[0] + 1)                                                                                                                                                                                                                              idx_start_end = np.array([[k[0], k[-1]] for k in sp])                                                                                                                                                                                                                                  sp_dur = (np.diff(idx_start_end, axis=1) / sf).flatten() * 1000                                                                                                                                                                                                                                      sp_amp, sp_freq = np.zeros(len(sp)), np.zeros(len(sp))                                                                                                                                                                                                                                           for i in range(len(sp)):                                                                                                                                                                                                                                                      sp_amp[i] = np.ptp(detrend(x[sp[i]]))  >                                                                                                                                                                                                                                                            sp_freq[i] = np.median((sf / (2 * np.pi) * np.diff(phase[sp[i]])))      A                                                                                                                                                                                                                                                                sp_params = {'Duration (ms)' : sp_dur, 'Frequency (Hz)': sp_freq,  7                                                                                                                                                                                                                                                                                              'Amplitude (uV)': sp_amp}      '                                                                                                                                                                                                                                                                    return supra_thresh_bool, sp_params5�_�                            ����                                                                                                                                                                                                                                                                                                                               
                 V   +    `P     �              5��