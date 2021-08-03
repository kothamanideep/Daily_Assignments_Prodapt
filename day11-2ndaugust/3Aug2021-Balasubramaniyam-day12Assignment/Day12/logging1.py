import logging

logging.basicConfig(filename='demo.log',level=logging.DEBUG)
x=int(input("Enter a number :"))
y=int(input("Enter a number :"))
try:
    logging.info(x//y)
except:
    logging.error("do not enter zero as denominator")

# logging.warning("Expected the integer Value") #50

# logging.error("An unknown error has happened")#40

# logging.critical("Critucal error as happened")#30

# logging.info("Normal page")#20

# logging.debug("its for developer ")#1