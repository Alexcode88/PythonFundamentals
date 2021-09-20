
# > < >= <= == != and  or not
# JavaScript       &&  ||  !

num = 18

if num > 10:
    print( "It is greater than 10" )
    print( "This will also print inside the if")

# print( "outside of the if" )

if num == 5:
    print( "It is exactly a 5")
elif num == 10: 
    print( "it is actually a 10" )
else:
    print( "it is a different number" )

#   if( num === 5 ){
#       console.log( "It is exactly a 5") 
#   }
#   else{
#       print( "it is a different number" )
#   }

if (num > 5 and num < 10):
    print( "It is in between 5 and 10 ")
