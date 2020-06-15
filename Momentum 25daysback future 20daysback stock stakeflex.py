


import numpy
#import pandas
count=0




#il primo def include anche i dati macroeco che pero non uso per ora anche perche bisogna scaricarli come ho fatto x i dati di mercato
#def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, VOL, USA_ADP, USA_EARN, USA_HRS, USA_BOT, USA_BC, USA_BI, USA_CU, USA_CF, USA_CHJC, USA_CFNAI, USA_CP, USA_CCR, USA_CPI, USA_CCPI, USA_CINF, USA_DFMI, USA_DUR, USA_DURET, USA_EXPX, USA_EXVOL, USA_FRET, USA_FBI, USA_GBVL, USA_GPAY, USA_HI, USA_IMPX, USA_IMVOL, USA_IP, USA_IPMOM, USA_CPIC, USA_CPICM, USA_JBO, USA_LFPR, USA_LMCI, USA_LEI, USA_MPAY, USA_MP, USA_NAHB, USA_NLTTF, USA_NFIB, USA_NFP, USA_NMPMI, USA_NPP, USA_EMPST, USA_PHS, USA_PFED, USA_PP, USA_PPIC, USA_RSM, USA_RSY, USA_RSEA, USA_RFMI, USA_TVS, USA_UNR, USA_WINV, exposure, equity, settings)
def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, VOL, exposure, equity, settings):
    global count, a, b
   
    #print(type(CLOSE))   #e un numpy.ndarray
    #print(CLOSE.shape)   #ha righe=loockback e colonne=numero dei markets che sono in considerazione qui:  settings['markets']  = ['CASH','F_DX', 'F_BO']
    nMarkets=CLOSE.shape[1] #return number of markets
    
    
    #x=numpy.zeros(CLOSE)
    #y=numpy.zeros(CLOSE)
   
 
    z=CLOSE[-1,0:]    #prendi l ultimo prezzo 
   
    w=CLOSE[-25,0:]   #prendi il penultimo prezzo tot. indietro
    
    #print(CLOSE)
    #print(z)
    #print(z[1])
    
    pos=numpy.zeros(nMarkets)   #inizializza la matrice con tutti zero su tutti i markets
    
    
    #count=(DATE[0])/(DATE[0])
    count=count+1
    #print(count)
    co=count%5
   
   
    indi=0
    counting2=7
    while counting2 !=0:
        counting2=counting2-1
        indi=indi+1
        if co==0 :
            
            if z[indi]>w[indi] and pos[indi]>=1:
                pos[indi]=pos[indi]+1
            elif z[indi]>w[indi] and pos[indi]<1:
                pos[indi]=1         
            elif z[indi]<w[indi] and pos[indi]<=-1:
                pos[indi]=pos[indi]-1      
            elif z[indi]<w[indi] and pos[indi]>-1:   
                pos[indi]=-1 

            
        
        else:
       
            pos[indi]=pos[indi]
            
    #print(pos)
      
       
    #print(pos)
    #print(exposure)
    
    return pos, settings


def mySettings():
    ''' Define your trading system settings here '''

    settings= {}

    # S&P 100 stocks
    # settings['markets']=['CASH','AAPL','ABBV','ABT','ACN','AEP','AIG','ALL',
    # 'AMGN','AMZN','APA','APC','AXP','BA','BAC','BAX','BK','BMY','BRKB','C',
    # 'CAT','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DIS','DOW',
    # 'DVN','EBAY','EMC','EMR','EXC','F','FB','FCX','FDX','FOXA','GD','GE',
    # 'GILD','GM','GOOGL','GS','HAL','HD','HON','HPQ','IBM','INTC','JNJ','JPM',
    # 'KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MON',
    # 'MRK','MS','MSFT','NKE','NOV','NSC','ORCL','OXY','PEP','PFE','PG','PM',
    # 'QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TWX','TXN','UNH','UNP',
    # 'UPS','USB','UTX','V','VZ','WAG','WFC','WMT','XOM']

    # Futures Contracts

    settings['markets']  = ['CASH', 'AMZN', 'AAPL', 'ACN', 'EBAY', 'GILD', 'GOOGL', 'CTSH']
    settings['beginInSample'] = '19900506'
    settings['endInSample'] = '20170506'
    settings['lookback']= 504
    settings['budget']= 10**6
    settings['slippage']= 0.05

    return settings

# Evaluate trading system defined in current file.
if __name__ == '__main__':
    import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)
