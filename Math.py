# Import nessessories
from numpy import mean, var, std, percentile, prod
from scipy.stats import skew

class Statistic(object):
    '''Class for computing various statistical measures on a sequence of numbers.'''

    domain = None

    def __init__(self, sequence) -> None:
        '''
        Initializes the Statistic object with a given sequence.

        Parameters:
        sequence (list or array-like): The sequence of numerical data.
        '''
        self.seq = sequence
        self.domain = max(self.seq) - min(self.seq)

    def Math_Mean(self) -> float:
        '''
        Computes the arithmetic mean of the sequence.

        Returns:
        float: The mean of the sequence.
        '''
        return float(mean(self.seq))

    def Geometric_Mean(self) -> float:
        '''
        Computes the geometric mean of the sequence.
        The geometric mean is the nth root of the product of all values in the sequence.

        Returns:
        float: The geometric mean of the sequence.
        '''
        # Compute the geometric mean as the nth root of the product of the sequence
        return float(prod(self.seq) ** (1/len(self.seq)))

    def Variance(self) -> float:
        '''
        Computes the variance of the sequence.

        Returns:
        float: The variance of the sequence.
        '''
        return float(var(self.seq))

    def Standard_Deviation(self) -> float:
        '''
        Computes the standard deviation of the sequence.

        Returns:
        float: The standard deviation of the sequence.
        '''
        return float(std(self.seq))

    def Coefficient_Of_Variation(self) -> float:
        '''
        Computes the coefficient of variation of the sequence.
        It is the ratio of the standard deviation to the mean, expressed as a float.

        Returns:
        float: The coefficient of variation of the sequence.
        '''
        return float(std(self.seq) / mean(self.seq))

    def Interquartile_Range(self) -> float:
        '''
        Computes the interquartile range (IQR) of the sequence.
        The IQR is the difference between the 75th percentile and the 25th percentile.

        Returns:
        float: The interquartile range of the sequence.
        '''
        q75, q25 = percentile(self.seq, [75, 25])
        return float(q75 - q25)

    def Skew(self) -> float:
        '''
        Computes the skewness of the sequence.
        Skewness measures the asymmetry of the data distribution.

        Returns:
        float: The skewness of the sequence.
        '''
        return skew(self.seq)
    
# Create an instance of the Statistic class
Stat = Statistic(range(1,11))
print('Result:')

# Loop through a list of tuples where each tuple contains:
# 1. A description of the statistical method being called (e.g., 'Math Mean')
# 2. The result of calling the corresponding method from the Statistic class instance
for res in [('Domain',Stat.domain),
            ('Math Mean', Stat.Math_Mean()),   
            ('Geometric Mean', Stat.Geometric_Mean()),   
            ('Variance', Stat.Variance()), 
            ('Standard Deviation', Stat.Standard_Deviation()),
            ('Coefficient Of Variation', Stat.Coefficient_Of_Variation()),  
            ('Interquartile Range', Stat.Interquartile_Range()),  
            ('Skewness', Stat.Skew())]:
    print(f'{res[0]}: {res[1]}\n{"-"*10}')