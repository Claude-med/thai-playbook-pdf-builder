# Contributing

Repository นี้เปิดให้แก้ไขและนำไปใช้ต่อได้ภายใต้ MIT License โดยขอให้รักษาความถูกต้องของ source credit, ลิขสิทธิ์สื่อ และคุณภาพภาษาไทย

## Workflow

1. Fork หรือ clone repository และสร้าง branch จาก `main`
2. แก้เฉพาะส่วนที่เกี่ยวข้องใน `SKILL.md`, `references/`, `assets/` หรือ `scripts/`
3. หากแก้ metadata ให้ปรับ `agents/openai.yaml` ให้ตรงกัน
4. รัน validation และ tests:

```bash
python tests/validate_skill.py
python -m unittest discover -s tests -v
```

5. เปิด pull request พร้อมอธิบายปัญหา วิธีแก้ และผลการทดสอบ

## Rules

- บันทึกไฟล์ข้อความเป็น UTF-8
- ห้าม commit transcript, outputs, browser profile, credentials หรือข้อมูลลูกค้า
- ห้ามเพิ่มภาพ โลโก้ หรือเนื้อหาบุคคลที่สามหากไม่มีสิทธิ์เผยแพร่
- รักษา CLI เดิม หรืออธิบาย breaking change อย่างชัดเจน
- เพิ่มหรือปรับ test เมื่อแก้พฤติกรรมของสคริปต์

Bug report และข้อเสนอควรมีตัวอย่าง input แบบย่อที่ไม่มีข้อมูลส่วนตัว และผลลัพธ์ที่คาดหวัง
