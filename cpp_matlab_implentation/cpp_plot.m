function CPP = cpp_plot( x, fs, normOpt)

%% Settings
filterType = 'highpass';
HPfilt_b = [1 - 0.97];
xLen = length( x );
frameLength = xLen;

frameLen = frameLength;
NFFT = 2 ^ ( ceil ( log (frameLen) / log(2) ) );
quef = linspace( 0, frameLen / 1000, NFFT );
F0lim = [ 333.3, 60 ]; 
quefLim = round(fs ./ F0lim);
quefSeq = ( quefLim(1):quefLim(2) )';

%% Apply filtering if requested
if strcmp( filterType, 'highpass' )
   x = filter( HPfilt_b, 1, x );
end

%% Create frame matrix
frameMat = zeros( NFFT,1);
frameMat(1:frameLen,1) = x;

%% Apply Hann window function
win = hanning(frameLen);
winMat = repmat( win,1,1 );
frameMat = frameMat(1:frameLen,:) .* winMat;

%% Compute magnitude spectrum
SpecMat = abs( fft( frameMat ) );
SpecdB = 10 * log10( SpecMat.^2 );

%% Compute log Cepstrum
Ceps = 10 * log10( abs( fft( SpecdB ) ).^2 );

%% Take quefrency range and compute max
CepsLim = Ceps( quefSeq,: );
[CepsMax,maxIdx] = max( CepsLim, [], 1 );

%% Do normalisation
CepsNorm = zeros( 1, 1);

if strcmp( normOpt, 'line' )
    p = polyfit( quefSeq, CepsLim(:,1), 1 );
    CepsNorm = polyval( p, quefSeq( maxIdx ) );
elseif strcmp( normOpt, 'nonorm' )==0
   CepsNorm = mean( CepsLim, 1 );
end

plot(quef(quefSeq), CepsLim, quef(quefSeq), polyval(p, quefSeq), 'o-', 'MarkerIndices', maxIdx, 'LineWidth',2.0)
title('Cepstrum')
xlabel('quefrency (s)') 
ylabel('log magnitude (dB)') 

CPP = CepsMax - CepsNorm;






