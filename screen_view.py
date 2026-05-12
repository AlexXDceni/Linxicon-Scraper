import pygetwindow as gw
import pyautogui
import pyperclip
import time
import json
import random


filler_list = [
    "mutation",
    "solution",
    "picture",
    "diamond",
    "courage",
    "fortune",
    "freedom",
    "harmony",
    "justice",
    "knowledge",
    "mystery",
    "passion",
    "serenity",
    "strength",
    "victory",
    "wisdom"
] 


def get_words(tab_name="Practice"):

    windows = [w for w in gw.getAllTitles() if tab_name.lower() in w.lower()]
    if not windows:
        print(f"The {tab_name} tab was not found!")
        return []

    win = gw.getWindowsWithTitle(windows[0])[0]
    win.activate()


    time.sleep(0.5)

    # pyautogui.press('esc')
    # pyautogui.click(win.left + 200, win.top + 200) 


    center_x = win.left + (win.width // 2)
    center_y = win.top + (win.height // 2)
    
    if center_x < 1 or center_y < 1:
        print("Coordonate fereastră invalide. Asigură-te că browserul este pe ecranul principal.")
        return None

    pyautogui.click(center_x, center_y)
    pyautogui.press('esc')
    time.sleep(0.5)


    # time.sleep(0.5)

    pyautogui.press('f12')

    time.sleep(1) 


    js_code = """
    (function() {
        const oldFetch = window.fetch;
        window.fetch = function(...args) {
            if (args[0] && args[0].includes('/api/updateGame')) {
                setTimeout(() => {
                    try {
                        const body = JSON.parse(args[1].body);

                        
                        

                        window.exportData = {
                        target: body.starters.tl.toUpperCase() + " - " + body.starters.br.toUpperCase(),
                        cuvinte: body.words.map(n => {
                            let group = "Deconected";
                            
                            if (n.color.includes('102, 143')) {
                                group = "Group A";
                            } else if (n.color.includes('209, 102')) {
                                group = "Group B";
                            } else if (n.color !== '#AAAAAA' && n.color !== 'rgb(170, 170, 170)') {
                                group = "Solved";
                            }

                            return {
                                word: n.word,
                                group: group,
                                hexColor: n.color
                            };
                        })

                        };
                        console.log("The data is ready in window.exportData");
                    } catch (e) { console.error(e); }
                }, 200);
            }
            return oldFetch.apply(this, args);
        };
        console.log(" Monitor active.");
    })();
"""
    pyperclip.copy(js_code)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    time.sleep(0.5)

    for _ in range(5): 
        pyautogui.hotkey('tab')        


    filler_word = random.choice(filler_list)
    print(f"Filler word: {filler_word}")

    pyautogui.write(filler_word, interval=0.1)
    pyautogui.press('enter')
    
    time.sleep(1)

    for _ in range(43): 
        pyautogui.hotkey('tab') 

    pyperclip.copy("copy(JSON.stringify(window.exportData))")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    time.sleep(0.5)

    CONTENT = pyperclip.paste()

    pyautogui.click(win.left + win.width // 2, win.top + win.height // 2)

    time.sleep(0.5)

    pyautogui.press('f12')
    
    time.sleep(0.5)

    try:
        INFO = json.loads(CONTENT)
        return INFO
    except:
        print("Error: Not a valid JSON format.")
        return None


