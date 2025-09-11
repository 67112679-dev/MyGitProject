import myfunc

def get_user_input():
    """ฟังก์ชันรับค่าจากผู้ใช้"""
    while True:
        try:
            a_input = input("กรุณาใส่ตัวเลขตัวแรก (A): ")
            a = myfunc.validate_input(a_input)
            if a is None:
                print("❌ กรุณาใส่ตัวเลขที่ถูกต้อง")
                continue
            
            b_input = input("กรุณาใส่ตัวเลขตัวที่สอง (B): ")
            b = myfunc.validate_input(b_input)
            if b is None:
                print("❌ กรุณาใส่ตัวเลขที่ถูกต้อง")
                continue
            
            return a, b
        except KeyboardInterrupt:
            print("\n\n👋 ขอบคุณที่ใช้โปรแกรม")
            exit()

def main():
    """ฟังก์ชันหลักของโปรแกรม"""
    print("🔢 โปรแกรมคำนวณการบวก")
    print("=" * 30)
    print("สร้างโดย: ณัฐดนัย หนูเนตร")
    print("รหัสนักศึกษา: 67112679")
    print("=" * 30)
    
    while True:
        # รับค่าจากผู้ใช้
        a, b = get_user_input()
        
        # คำนวณผลลัพธ์
        result = myfunc.add_numbers(a, b)
        
        # แสดงผลลัพธ์
        print("\n✅ ผลลัพธ์:")
        print(myfunc.format_result(a, b, result))
        print()
        
        # ถามว่าต้องการคำนวณต่อหรือไม่
        while True:
            continue_calc = input("คำนวณต่อหรือไม่? (y/n): ").lower().strip()
            if continue_calc in ['y', 'yes', 'ใช่']:
                print()
                break
            elif continue_calc in ['n', 'no', 'ไม่']:
                print("\n👋 ขอบคุณที่ใช้โปรแกรม")
                return
            else:
                print("กรุณาใส่ 'y' หรือ 'n'")

if __name__ == "__main__":

    main()
