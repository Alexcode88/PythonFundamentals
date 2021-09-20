

# function addTwoNumbers( n1, n2 ){
#     let total = n1 + n2;
#     return total;
# }

def addTwoNumbers( n1 = 0, n2 = 0):
    total = n1 + n2
    return total

#result = addTwoNumbers( 10, 20 )
#print( result )

result2 = addTwoNumbers( 0, 50 )
#print( result2 )

def changeValue( dictionary ):
    newDictionary = {
        'extra' : 'Extra value'
    }
    dictionary.update( newDictionary  )

x = {
    'one' : 1,
    'two' : 2
}

changeValue( x )

print( x )