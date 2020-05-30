import PIL
import tensorflow as tf
from matplotlib import pyplot as plt
import pynput
import cv2
import numpy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pickle

#/--------------------------------------paths&vars--------------------------------------/

url = 'chrome://dino'
chrome_driver_path = 'C:\\Users\\Mayur\\source\\tools\\chromedriver.exe'
loss_file_path = "/Assets/loss_df.csv"
actions_file_path = "/Assets/actions_df.csv"
q_value_file_path = "/Assets/q_values.csv"
scores_file_path = "/Assets/scores_df.csv"
init_script = "document.getElementsByClassName('runner-canvas')[0].id = 'runner-canvas'"
getbase64Script = "canvasRunner = document.getElementById('runner-canvas'); \
return canvasRunner.toDataURL().substring(22)"

#/--------------------------------------SLEENIUM_AND_BROWSER_INTERFACE--------------------------------------/

class sbi:
    def __init__(self, custom_config=True):
        chrome_options = Options()
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("mute_audio")
        self._driver = webdriver.Chrome(executable_path = chrome_driver_path, chrome_options = chrome_options)
        self._driver.set_window_position(x=-10,y=0)
        self._driver.get('chrome://dino')
        self._driver.execute_script("Runner.config.ACCELERATION=0")
        self._driver.execute_script(init_script)
    def crash(self):
        return _driver.execut_script("return Runner.instance_.crashed")
    def playing(self):
        return _driver.execut_script("return Runner.instance_.playing")
    def restart(self):
        return _driver.execut_script("return Runner.instance_.restart()")
    def up(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)
    def score(self):
        score_array = self._driver.execute_script("return Runner.instance_.distance_meter.digits")
        score = ''.join(score_array)
        return int(score)
    def pause(self):
        return _driver.execut_script("return Runner.instance_.stop()")
    def resume(self):
        return _driver.execut_script("return Runner.instance_.play()")
    def end(self):
        return _driver.execut_script("return Runner.instance_.stop()")

#/--------------------------------------AGENT--------------------------------------/

class agent:
    def __init__(self, sbi):
        self._sbi = sbi
        self.jump()
    def is_running(self):
        return self._sbi.get_playing()
    def is_crashed(self):
        return self._sbi.get_crashed()
    def jump(self):
        self._sbi.press_up()
    def duck(self):
        self._sbi.press_down()

#/--------------------------------------GETTING_STATE_OF_GAME--------------------------------------/

class state:
    def _init_(self, sbi, agent):
        self._agent = agent
        self._sbi = sbi
        self._display = show_img()
        self._display.__next__()
    def get_state(self,actions):
        actions_df.loc[len(actions_df)] = actions[1]
        score = self._sbi.get_score() 
        reward = 0.1
        is_over = False 
        if actions[1] == 1:
            self._agent.jump()
        image = grab_screen(self._sbi._driver) 
        self._display.send(image) 
        if self._agent.is_crashed():
            scores_df.loc[len(loss_df)] = score 
            self._sbi.restart()
            reward = -1
            is_over = True
        return image, reward, is_over
        
#/--------------------------------------FILE_SAVING_AND_LOADING--------------------------------------/
def save_obj(obj, name):
    with open('objects/'+ name + '.pkl', 'wb') as f: 
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_obj(name):
    with open('objects/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def grab_screen(_driver):
    image_b64 = _driver.execute_script(getbase64Script)
    screen = np.array(Image.open(BytesIO(base64.b64decode(image_b64))))
    image = process_img(screen)
    return image

def process_img(image):
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    image = image[:300, :500] 
    image = cv2.resize(image, (80,80))
    return  image

def show_img(graphs = False):
    while True:
        screen = (yield)
        window_title = "logs" if graphs else "game_play"
        cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)        
        imS = cv2.resize(screen, (800, 400)) 
        cv2.imshow(window_title, screen)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.destroyAllWindows()
            break    
loss_df = pd.read_csv(loss_file_path) if os.path.isfile(loss_file_path) else pd.DataFrame(columns =['loss'])
scores_df = pd.read_csv(scores_file_path) if os.path.isfile(loss_file_path) else pd.DataFrame(columns = ['scores'])
actions_df = pd.read_csv(actions_file_path) if os.path.isfile(actions_file_path) else pd.DataFrame(columns = ['actions'])
q_values_df =pd.read_csv(actions_file_path) if os.path.isfile(q_value_file_path) else pd.DataFrame(columns = ['qvalues'])

def init_cache():
    save_obj(INITIAL_EPSILON,"epsilon")
    t = 0
    save_obj(t,"time")
    D = deque()
    save_obj(D,"D")

def buildmodel():
    print("Now we build the model")
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Conv2D(32, (8, 8), activation = 'relu', input_shape = (80, 80, 1)))
    model.add(tf.keras.layers.Maxpooling2D((2, 2)
              )
    model.add(tf.keras.layers.Conv2D(64, (8, 8), activation = 'relu')
              )
    model.add(tf.keras.layers.Maxpooling2D((2, 2)
                                           )
              )
    model.add(tf.keras.layers.Conv2D(64, (8, 8), activation = 'relu')
              )
    model.add(tf.keras.layers.Maxpooling2D((2, 2)
                                           )
              )
