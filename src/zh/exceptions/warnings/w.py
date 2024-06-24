import warnings
# 正常情况下，下面的警告不会显示
warnings.warn('警告', ImportWarning)
# 正常情况下，下面的警告不会作为异常被抛出
warnings.warn('Err 抛出异常')