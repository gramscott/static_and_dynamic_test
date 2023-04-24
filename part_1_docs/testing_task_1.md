### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  def check_for_ace(self, card):       
    if card.value = 1:  # The = needs to be swapped for a == for a comparison 
      return True
    else# else needs to have a colon afterwards. 
      return False


  dif highest_card(self, card1 card2):# LINE 31: dif should be def. Comma after card1
  if card1.value > card2.value:
    return card  # card should be card1 in the return, so it matches the argument that was used in the parameter. 
  else:
    return card2



# after fixing the dif to a def there needs to be an indent for the if needs to be a space forward. # because the last function is a "dif" then it ruins the next test.
def cards_total(self, cards):
  total# LINE 43: total needs to = to a value so it can be used.
  for card in cards:
    total += card.value   # Delete value.
  return "You have a total of" + total
    # the total should be covered in str{} 
    # the return needs to be outside the for loop



```
