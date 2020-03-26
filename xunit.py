# encoding: utf-8

class TestCase:
    # コンストラクタ
    def __init__(self,name):
        self.name = name
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            # 2つ目のかっこに指定された引数を満たした状態で宣言すると，とりあえず関数が実行される．
            # 関数に返り値がない場合はNoneTypeになり，もう一回関数として呼ぼうとしても失敗する．
            # 逆に引数を与えずに実行すると関数が代入される．
            # 危険
            method = getattr(self,self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "
    def testMethod(self):
        self.log = self.log + "testMethod "
    def testBrokenMethod(self):
        raise Exception
    def tearDown(self):
        self.log = self.log + "tearDown "

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod") #WasRunインスタンス生成
        test.run()
        assert("setUp testMethod tearDown " == test.log)
    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        # print("result.summary()")
        # print(result.summary())
        assert("1 run, 1 failed" == result.summary())

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def testFailed(self):
        self.errorCount = self.errorCount + 1
    def summary(self):
        print(self.errorCount)
        return "%d run, %d failed" % (self.runCount, self.errorCount)

# print(TestCaseTest("testTemplateMethod").run().summary())
# print(TestCaseTest("testResult").run().summary())
# print(TestCaseTest("testFailedResult").run().summary())
print(TestCaseTest("testFailedResultFormatting").run().summary())