from Functions import *

def test_hello_freud():
    assert callable(hello_freud)
    input_string = 'hello'
    output = hello_freud(input_string)
    assert output == 'Hello there. I am Sigmund Freud, the father of psychoanalysis. Ask me for a fun fact, or say \'quit\' to end the chat.'
    
def test_give_fun_facts():
    assert callable(give_fun_facts)
    input_string = 'fun fact'
    fun_fact_list = ['Psychoanalysis was founded in the 1890s in Vienna.', 
                     'The key to psychoanaylsis is making the unconscious, conscious.', 
                     'Psychoanalytic psychologists believed that causes of mental illnesses were repressed traumatic experiences.' 
                     'One method of psychoanalysis is an ink blot test, in which a client \'projects\' from their unconscious/subconscious mind to interpret what they are being shown.', 
                     'One of the most famous psychoanalytic theories is called the Oedipus Complex. I, (Sigmund Freud), introduced this theory which states that during one stage of development, one would desire sexual involvement with the parent of the opposite sex and feel rivalry towards the parent of the same sex.',   
                     'A Freudian slip occurs when someone states what is actually on their mind instead of what they intended to say. In pop culture, a Freudian slip usually involves something sexual being stated as what is really on someone\'s mind rather than the intended wholesome or SFW statement.',  
                     'I (Sigmund Freud) believed that the best way to discover one\'s unconscious was through the analysis of dreams. The conscious mind acts a censor on the true content hidden in the unconscious. My famous book, The Interpretation of Dreams, elaborates on the concept of dream analysis.', 
                     'I (Sigmund Freud) proposed a female psychosexual stage of development called penis envy. I believe that young girls experience anxiety upon the discovery of the fact that they do not have a penis. Conversely, a boy would experience castration anxiety after realizing that women do not have a penis.', 
                     'I (Sigmund Freud) devised a set of defense mechanisms to describe the psychological resistance one might display when trying to bring the unconscious into the conscious. Some of these defense mechanisms are still widely referenced in pop culture today, such as: repression, projection, and denial.', 
                     'The stereotypical portrayal of psychologists and psychiatrists in pop culture (a client lays on a couch and talks while the doctor scribbles notes, hidden from the client\'s view) can be attributed to psychoanalysis. Psychoanalysts maintain a distant relationship with clients in order for that space to be more occupied by the client\'s unconscious, safe from outside interference.']
    output = give_fun_facts(input_string)
    assert output in fun_fact_list
    
def test_freud_bot():
    assert callable(freud_bot)
