from pyscript import document, display

def check_team(e): #get team
    regi_el = document.querySelector('input[name="regi"]:checked')
    medi_el = document.querySelector('input[name="medi"]:checked')

    #nothing selected
    if not regi_el or not medi_el:
        display("Please answer all Yes/No questions.", target="Output")
        return
    regi = regi_el.value
    medi = medi_el.value
    gr = document.getElementById("gr").value
    sec = document.getElementById("sec").value

    if regi == "Yes":
        if medi == "Yes":
            if gr == "7" or gr == "8" or gr == "9":
                if sec == "Sap":
                    display("You are Yellow Tigers, Roar", target="#Output", append=False)
                elif sec == "Ruby":
                    display("You are Green Hornets, Buzz", target="#Output", append=False)
                elif sec == "Top":
                    display("You are Red Bulldogs, Arf", target="#Output", append=False)
                elif sec == "Eme":
                    display("You are Blue Bears, Growl", target="#Output", append=False)
                elif sec == "Jade":
                    display("You are Green Hornets, Buzz", target="#Output", append=False)
            elif gr == "10":
                if sec == "Sap":
                    display("You are Yellow Tigers, Roar", target="#Output", append=False)
                elif sec == "Ruby":
                    display("You are Green Hornets, Buzz", target="#Output", append=False)
                elif sec == "Top":
                    display("You are Red Bulldogs, Arf", target="#Output", append=False)
                elif sec == "Eme":
                    display("You are Blue Bears, Growl", target="#Output", append=False)
        else:
            display("Get medical clearance first.", target="#Output", append=False)    
    elif regi == "No":
        display("Register first.", target="#Output", append=False)

    else:
        display("Fill up everything.", target="#Output", append=False)   