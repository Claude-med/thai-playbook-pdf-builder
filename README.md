# Thai Playbook PDF Builder

Codex skill สำหรับสร้าง ปรับปรุง และตรวจคุณภาพ Thai Simple Action Playbook ของ Claude Work TH จาก transcript, brief, notes, article, podcast หรือแหล่งข้อมูลสนับสนุน

Repository นี้ตั้งใจให้ส่งต่อได้สองแบบ:

- **ใช้งานทันที**: ติดตั้ง skill แล้วเรียก `$thai-playbook-pdf-builder`
- **แก้ไขต่อ**: clone repository, ปรับคำสั่ง/แม่แบบ/QA แล้วทดสอบก่อนส่งกลับด้วย pull request

## ติดตั้ง

### ให้ Codex ติดตั้งให้

ส่งคำสั่งนี้ให้ Codex:

```text
ติดตั้ง skill จาก https://github.com/Claude-med/thai-playbook-pdf-builder/tree/main/skills/thai-playbook-pdf-builder
```

### ติดตั้งด้วยคำสั่ง

macOS/Linux:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Claude-med/thai-playbook-pdf-builder \
  --path skills/thai-playbook-pdf-builder
```

Windows PowerShell:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" `
  --repo Claude-med/thai-playbook-pdf-builder `
  --path skills/thai-playbook-pdf-builder
```

Restart Codex หลังติดตั้งเพื่อให้ระบบพบ skill ใหม่

## ตัวอย่างการใช้งาน

```text
$thai-playbook-pdf-builder สร้าง playbook ภาษาไทยจาก transcript ในโฟลเดอร์นี้
กลุ่มเป้าหมายคือเจ้าของธุรกิจมือใหม่ ต้องการ PDF 24 หน้า พร้อม prompt pack และ source credit
```

```text
$thai-playbook-pdf-builder ตรวจ playbook package นี้และแก้ปัญหาโครงสร้าง ภาษาไทย และ PDF layout ให้พร้อมเผยแพร่
```

Skill จะใช้ source audit, research notes และ playbook blueprint เป็น planning gates ก่อนสร้าง final package และจะไม่คัดลอก transcript หรือภาพบุคคลที่สามแบบยาวโดยไม่มีสิทธิ์

## PDF QA

ใช้ Python 3.10 ขึ้นไป และติดตั้ง dependency:

```bash
python -m pip install -r requirements-qa.txt
```

ตรวจโครงสร้าง package:

```bash
python skills/thai-playbook-pdf-builder/scripts/audit_playbook_package.py path/to/outputs --strict
```

render ทุกหน้าเพื่อตรวจด้วยสายตา:

```bash
python skills/thai-playbook-pdf-builder/scripts/render_pdf_qa.py path/to/playbook.pdf --out path/to/qa_pages
```

ถ้าโฟลเดอร์ QA มีไฟล์จากรอบก่อน ให้เพิ่ม `--force` สคริปต์จะลบเฉพาะ `page-NN.png` และ `contact_sheet.jpg` ที่ตัวเองสร้าง

## แก้ไข Skill ต่อ

โครงสร้างหลัก:

```text
skills/thai-playbook-pdf-builder/
|-- SKILL.md                 # workflow และกติกาหลัก
|-- agents/openai.yaml       # ชื่อ คำอธิบาย และ default prompt ใน UI
|-- assets/                  # แม่แบบที่นำไปใช้สร้าง output
|-- references/              # rubric และรายละเอียดที่โหลดเมื่อจำเป็น
`-- scripts/                 # deterministic QA tools
```

Workflow ที่แนะนำ:

```bash
git clone https://github.com/Claude-med/thai-playbook-pdf-builder.git
cd thai-playbook-pdf-builder
git switch -c improve/short-description
python tests/validate_skill.py
python -m unittest discover -s tests -v
```

เมื่อแก้ชื่อ, description หรือ default prompt ให้ตรวจ `agents/openai.yaml` ให้ตรงกับ `SKILL.md` ด้วย ดูกติกาเพิ่มเติมใน [CONTRIBUTING.md](CONTRIBUTING.md)

## English Quick Start

Install the skill from `Claude-med/thai-playbook-pdf-builder`, restart Codex, then invoke `$thai-playbook-pdf-builder`. The skill creates and reviews practical Thai A4 playbooks with source auditing, research traceability, beginner-first writing, companion assets, and PDF QA.

To contribute, clone the repository, create a branch, run `python tests/validate_skill.py` and `python -m unittest discover -s tests -v`, then open a pull request.

## License

[MIT](LICENSE). Source materials, third-party images, trademarks, and brand assets remain subject to their respective owners' rights.
