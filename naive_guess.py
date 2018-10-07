# A naive way to guess a number

number_to_be_guessed = 10

attempt = 0
start = 0
end = 100
while True:
    guessed_number = random.randint(start,end)
    if guessed_number == number_to_be_guessed:
        print("Number found, which is {}".format(guessed_number))
        break
    elif guessed_number > number_to_be_guessed:
        end = guessed_number
    else:
        start = guessed_number   
    print("Attempt:{} -- Guessed Number:{} -- Start Value:{} -- End Value:{}"\
      .format(attempt,guessed_number,start,end))
    attempt += 1
