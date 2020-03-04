# encoding: utf-8

class TestCase:
    # コンストラクタ
    def __init__(self,name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        # 2つ目のかっこに指定された引数を満たした状態で宣言すると，とりあえず関数が実行される．
        # 関数に返り値がない場合はNoneTypeになり，もう一回関数として呼ぼうとしても失敗する．
        # 逆に引数を与えずに実行すると関数が代入される．
        # 危険
        method = getattr(self,self.name)
        method()

class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod") #WasRunインスタンス生成
    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)
    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()