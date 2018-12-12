def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


# uma alternativa é:

def generate_password():
    return ''.join(random.sample(word_list,3))

