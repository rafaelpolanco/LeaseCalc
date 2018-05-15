# -*- coding: utf-8 -*-
"""
Created on Thu May  3 15:20:55 2018

@author: Rafael
"""

class LeaseCalc:    
    def __call__(self, 
               msrp, 
               capitalizationCost, 
               residualPerc, 
               term,
               moneyFactor,
               localTaxRate):
         self.msrp = msrp
         self.capitalizationCost = capitalizationCost
         self.residualPerc = residualPerc
         self.term = term
         self.moneyFactor = moneyFactor
         self.localTaxRate = localTaxRate
         
         self.calc()
        
    def calc(self):
        self.residual = self.calcResidual(self.msrp, self.residualPerc)
        self.depositionCharge = self.calcDepositionCharge(
                                    self.capitalizationCost, 
                                    self.residual, 
                                    self.term)
        self.interestRate = self.calcInterestRate(self.moneyFactor)
        self.financeCharge = self.calcFinanceCharge(self.capitalizationCost,
                                                    self.residual,
                                                    self.moneyFactor)
        self.payment = self.calcPayment(self.depositionCharge, self.financeCharge)
        self.tax = self.calcTax(self.payment, self.localTaxRate)
        self.totalPayment = self.calcTotalPayment(self.payment, self.tax)
        
    def calcResidual(self, msrp, residualPerc):
        return msrp * residualPerc
    
    def calcDepositionCharge(self, capitalizationCost, residual, term):
        return (capitalizationCost - residual) / term

    def calcInterestRate(self, moneyFactor):
        return moneyFactor * 2400
    
    def calcFinanceCharge(self, capitalizationCost, residual, moneyFactor):
        return (capitalizationCost + residual) * moneyFactor
    
    def calcPayment(self, depositionCharge, financeCharge):
        return depositionCharge + financeCharge
    
    def calcTax(self, payment, localTax):
        return payment * localTax
    
    def calcTotalPayment(self, payment, tax):
        return payment + tax
    
