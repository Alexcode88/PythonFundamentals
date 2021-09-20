# A comment goes here
# // A comment goes here in JS

num = 20            # let num = 20;
flag = True         # let flag = true;
name = 'Alfredo'    # let name = "Alfredo";  

nums = [10, 20, 30, 40, 50] # let nums = [10, 20, 30, 40, 50];

# Touple (a list of constant values)
names = ( "Alfredo", "Alexander", "Marcelo", "Sofia", "Valeria" )

print( num )        # console.log( num )
print( flag )
print( name )
print( nums )
print( names )

# Basically the same as in JS
car = {
    'make' : 'Honda',
    'year' : 2018,
    'name' : 'CRV'
}

print( car )

# Whole numbers - int
# Decimal numbers - float
whole = 30
decimal = 8.63

# Number( decimal ) JS

print( type( whole ) )      # typeof( whole )
print( type( decimal ) )

turnToInt = int( decimal )  

print( turnToInt )

turnToFloat = float( whole )

print( turnToFloat )

firstName = "Alfredo"
lastName = "Salazar"

fullName = firstName + " " + lastName + str( num )

print( fullName )

# ` Hey there class my name is ${firstName} ${lastName}`
print( f"{num}Hey there class my name is {firstName} {lastName}. Nice to meet you!" )

print( "{}Hey there class my name is {} {}. Nice to meet you!".format(num, firstName, lastName ))

print( "%dHey there class my name is %s %s. Nice to meet you!" % (num, firstName, lastName))