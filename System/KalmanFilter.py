# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:17:22 2021

@author: bjahu
"""



def kalman_filter(processNoise,measurementNoise,dbm):
        estimatedRSSI=0
        pestimatedRSSI=0
        errorCovarianceRSSI=0
        isInitialized = True    
        priorRSSI=0
        kalmanGain=0
        priorErrorCovarianceRSSI=1
        if isInitialized== False:
             priorRSSI = dbm
             priorErrorCovarianceRSSI=1
             isInitialized= True
        else :
            priorRSSI = dbm
            priorErrorCovarianceRSSI = errorCovarianceRSSI + processNoise
            
        kalmanGain = priorErrorCovarianceRSSI / (priorErrorCovarianceRSSI + measurementNoise)
        estimatedRSSI = priorRSSI + (kalmanGain * (dbm - priorRSSI))
        errorCovarianceRSSI = (1 - kalmanGain) * priorErrorCovarianceRSSI
        return estimatedRSSI
    
    
    
    
    
    
    
print(kalman_filter(0.125, 0.8, -70))