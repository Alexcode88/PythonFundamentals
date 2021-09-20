car = {
    'make' : 'Honda',
    'year' : 2018,
    'name' : 'CRV',
    'models' : {
        'model1' : 'LE',
        'modle2' : 'XE'
    }
}

info = {
    'price' : 120000
}

print( car['year'] )

print( car['models']['model1'] )

car.pop( 'models' )
car.update( info )

print( car )