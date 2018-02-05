class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]
        
        carry = 0
        c = ""
        for i in range(len(a)):
            b_val = int(b[i]) if i < len(b) else 0
            if int(a[i]) + b_val + carry == 3:
                carry = 1
                c += "1"
            elif int(a[i]) + b_val + carry == 2:
                carry = 1
                c += "0"
            elif int(a[i]) + b_val + carry == 1:
                carry = 0
                c += "1"
            else:
                carry = 0
                c += "0"
           #  except:
               #  break
        if carry == 1:
            c += "1"
            
        return c[::-1]