# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:21:29 2018

@author: Rafael
"""

import LeaseCalc


def main():
    
    calc = LeaseCalc.LeaseCalc()
    
    calc(55800,53800, 0.56, 42, 0.00088, 0.0825)
    
    print("")
    print("INPUT VALUES")
    print("------------")
    print("MSRP: " + str(calc.msrp))
    print("Cap. Cost: " + str(calc.capitalizationCost))
    print("Res. Perc.: " + str(calc.residualPerc))
    print("Term: " + str(calc.term))
    print("Money Factor: " + str(calc.moneyFactor))
    print("Local Tax Rate: " + str(calc.localTaxRate))
    
    print("")
    print("OUTPUT VALUES")
    print("-------------")
    print("Residual: " + str(calc.residual))
    print("Dep. Charge: " + str(calc.depositionCharge))
    print("Interest Rate: " + str(calc.interestRate))
    print("Finance Charge: " + str(calc.financeCharge))
    print("Payment: " + str(calc.payment))
    print("Tax: " + str(calc.tax))
    print("Total Payment: " + str(calc.totalPayment))
    
if __name__ == "__main__":
    main()