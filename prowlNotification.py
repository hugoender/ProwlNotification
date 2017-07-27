import prowlpy

myApiKey = '123456789'
p = prowlpy.Prowl(myApiKey)

voltageLevel = 3.4
totalTestTime = 2332.23

try:
    p.add('Battery Life Test',
        'Voltage is at: %s V' % voltageLevel,
        'Test has been running for: %s seconds' % totalTestTime,
        1,
        None,
        "website")
except Exception, msg:
    print msg