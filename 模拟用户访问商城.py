import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ch_options = Options()
# 无头模式 不用打开浏览器
ch_options.add_argument("--headless")

chromedriver_path = "/Users/corleone/projects/chromedriver"
# 这个driver一定要设置为全局变量，否则浏览器会闪退
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=ch_options)

wait = WebDriverWait(driver, 10)


def main(user_num):
    try:
        sleep_time = 0.5
        # 打开页面
        driver.get('http://localhost:9528/login')
        # 等待页面加载完成
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("username").send_keys("admin", user_num)  # 模拟按键输入
        driver.find_element_by_id("password").send_keys("123456")  # 模拟按键输入
        driver.find_element_by_id("login-btn").click()  # 模拟鼠标点击
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-image")))

        images = driver.find_elements(By.CLASS_NAME, "product-image")
        random.shuffle(images)
        click_num = random.randint(0, 10)
        # 如果随机数不为0，则进行点击操作
        if click_num > 0:
            for j in range(click_num):
                images = driver.find_elements(By.CLASS_NAME, "product-image")
                if j >= len(images):
                    continue
                images[j].click()
                # # 这里跳转到了商品详情页，每次页面变动都要sleep一下，否则获取不到元素
                wait.until(
                    EC.presence_of_element_located((By.XPATH, '//p[@data-v-7f8130ba="" and contains(text(), "库存")]')))
                driver.back()
                time.sleep(sleep_time)
                print("click_num: ", j)

        print("total_click_num: ", click_num)

        # 找到页面中加入购物车按钮
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button/span[text()='加入购物车']")))
        button = driver.find_elements_by_xpath("//button/span[text()='加入购物车']")
        # 从0-10随机
        # random.shuffle(button)
        add_cart_num = random.randint(0, 5)
        # 如果随机数为0，直接退出
        if add_cart_num == 0:
            print("add_cart_num is 0")
            # 登出
            button = driver.find_element_by_xpath("//button/span[text()=' 登出 ']")
            button.click()
            wait.until(EC.presence_of_element_located((By.ID, "username")))
            print("未进入购物车登出")
            return
        for j in range(add_cart_num):
            print("add: ", j)
            button[j].click()
        print("total_add_: ", add_cart_num)
        # 0到1 随机 如果是0 退出，否则进入购物车
        random_num = random.randint(0, 5)
        if random_num == 0:
            # 登出
            button = driver.find_element_by_xpath("//button/span[text()=' 登出 ']")
            button.click()
            wait.until(EC.presence_of_element_located((By.ID, "username")))
            print("未购物车后登出")
            return
        # 进入购物车
        time.sleep(sleep_time)
        # button = driver.find_element_by_xpath("//button/span[text()=' 购物车 ']")
        # button.click()
        # 无头模式下通过点击有可能点到navbar，可能是太快了的事儿吧，所以这里改成用链接访问购物车
        driver.get("http://localhost:9528/#/cart")
        # 等待购物车页面加载完成
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button/span[text()='提交订单']")))
        # 获取所有的移除按钮 随机取N个
        remove_buttons = driver.find_elements_by_xpath("//button/span[text()='移除']")
        random_num = random.randint(0, len(remove_buttons) - 1)
        for j in range(random_num):
            print("remove: ", j)
            remove_buttons = driver.find_elements_by_xpath("//button/span[text()='移除']")
            if j >= len(remove_buttons):
                continue
            remove_buttons[j].click()
            time.sleep(sleep_time)
        random_num = random.randint(0, 3)
        if random_num == 0:
            # 登出
            button = driver.find_element_by_xpath("//button/span[text()=' 登出 ']")
            button.click()
            wait.until(EC.presence_of_element_located((By.ID, "username")))
            print("未提交订单而登出")
            return
        # 提交订单
        print("total_remove_num: ", random_num)
        button = driver.find_element_by_xpath("//button/span[text()='提交订单']")
        button.click()
        # 0-1随机 如果是0 选择支付宝，否则选择微信
        random_num = random.randint(0, 1)
        if random_num == 0:
            button = driver.find_element_by_xpath("//label/span[text()='支付宝']")
            button.click()
        else:
            button = driver.find_element_by_xpath("//label/span[text()='微信']")
            button.click()
        # 点击确定
        button = driver.find_element_by_xpath("//button/span[text()='确定']")
        button.click()
        # 等待支付完成变成暂无商品
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[text()='暂无商品']")))
        # 登出
        button = driver.find_element_by_xpath("//button/span[text()=' 登出 ']")
        button.click()
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        print("到最后登出")
    except Exception as e:
        print(e)
        button = driver.find_element_by_xpath("//button/span[text()=' 登出 ']")
        button.click()
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        print("报错后登出")


# if __name__ == "__main__": 语句是必要的，因为它可以确保 main() 函数仅在主模块中执行。
# 如果将 if __name__ == "__main__": 语句删除，则 main() 函数将在任何导入该模块的模块中执行。这可能会导致意外的结果，例如打开多个 Google 首页。
if __name__ == "__main__":
    for i in range(1000):
        print("userNum: ", i)
        main(i + 1)
