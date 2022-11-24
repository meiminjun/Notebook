# 常见异常问题处理

## 递归时要在except返回

> - 有finally 有return 一定会执行
> - 没有return 就会在try 位置返回


```python
def exceptTest(code=1):
    try:
        print('doing some work, and maybe exception will be raised')
        if code < 5:
            code += 1
            raise KeyError('index error')
            print('after exception raise')
        return 111
    except KeyError as e:
        print('in KeyError except')
        print(e)
        return exceptTest(code)
    except IndexError as e:
        print('in IndexError except')
        print(e)
        return 2
    except ZeroDivisionError as e:
        print('in ZeroDivisionError')
        print(e)
        return 3
    finally:
        print('in finally')
        # return 5


resultCode = exceptTest()
print(resultCode)
```

    doing some work, and maybe exception will be raised
    in KeyError except
    'index error'
    doing some work, and maybe exception will be raised
    in KeyError except
    'index error'
    doing some work, and maybe exception will be raised
    in KeyError except
    'index error'
    doing some work, and maybe exception will be raised
    in KeyError except
    'index error'
    doing some work, and maybe exception will be raised
    in finally
    in finally
    in finally
    in finally
    in finally
    111


## 参考

- https://www.cnblogs.com/JohnABC/p/4065437.html#:~:text=%E5%AD%A6%E4%B9%A0python%E6%88%96%E8%80%85%E5%85%B6%E4%BB%96%E6%9C%89%E5%BC%82%E5%B8%B8%E6%8E%A7%E5%88%B6%E7%9A%84%E7%BC%96%E7%A8%8B%E8%AF%AD%20%E8%A8%80%EF%BC%8C%20%E5%A4%A7%E5%AE%B6%E5%BE%88%E6%9C%89%E5%8F%AF%E8%83%BD%E8%AF%B4try%20except%20finally%EF%BC%88try,catch%20finally%EF%BC%89%E7%9A%84%E6%89%A7%E8%A1%8C%E5%BE%88%E7%AE%80%E5%8D%95%EF%BC%8C%E6%97%A0%E9%9D%9E%E5%B0%B1%E6%98%AF%E6%9C%89%E5%BC%82%E5%B8%B8%E7%9A%84%E8%AF%9D%E6%89%A7%E8%A1%8Cexcept%EF%BC%8C%20finally%E6%97%A0%E8%AE%BA%E6%98%AF%E5%90%A6%E6%9C%89%E5%BC%82%E5%B8%B8%E9%83%BD%E4%BC%9A%E6%89%A7%E8%A1%8C%EF%BC%8C%20%E5%A4%A7%E8%87%B4%E4%B8%8A%E5%8E%9F%E5%88%99%E6%98%AF%E8%BF%99%E6%A0%B7%EF%BC%8C%20%E4%BD%86%E6%98%AF%E5%A6%82%E6%9E%9C%E6%B6%89%E5%8F%8A%E5%88%B0%E6%9B%B4%E5%8A%A0%E8%AF%A6%E7%BB%86%E7%9A%84%E5%A4%8D%E6%9D%82%E7%9A%84%E8%B7%AF%E5%BE%84%EF%BC%8C%E5%8A%A0%E4%B8%8Areturn%20%E8%AF%AD%E5%8F%A5%EF%BC%8C%E5%B0%B1%E6%B2%A1%E6%9C%89%E9%82%A3%E4%B9%88%E7%AE%80%E5%8D%95%E4%BA%86%E3%80%82
