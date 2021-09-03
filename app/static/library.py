from org.transcrypt.stubs.browser import *
# import random

para_list = []


def grab_parameters():
	'''	This function is grab the parameters from the website for the loan inputs.
    
        Examples
        --------
		You could to do the following:
		- Loan amount($) : 440248
        - Tenor (Years): 30

		- Fixed Rate (Package)
            - Interest Rates(%): 2.6
            - Term Periods (Years): 30 (automatically assumed)
            
		- "Market/Variable" Rate (Package)
        - Interest Rates (list) and Term Period (list) should be of the same length
        - If being offered 1.39% for Year 1; 1.48% for Year 2-5 and 2.3% After Year 5
            - Interest Rates(%): 1.39,1.48,2.3
            - Representing end years i.e. Up to Year 1, Up to Year 5, Up to Year 6
            - Term Periods (Years): 1,5,6
            

	'''

	loanAmount = document.getElementById("loanAmount").value
	loanTenor = document.getElementById("loanTenor").value
	interestRate = document.getElementById("interestRate").value
	termPeriod = document.getElementById("termPeriod").value
	console.log(loanAmount,loanTenor,interestRate,termPeriod)
	# console.log(loanAmount)
	global para_list
	para_list.extend([loanAmount,loanTenor,interestRate,termPeriod])

