#!/usr/bin/env python3
"""
批量修改所有文件中过于具体的"Cursor/Copilot"工具名，
替换为更通用的描述，与 Web 版本对齐。

保留不改：
- "Data Copilot"（阿里云产品名，非泛指）
- "给每个人发一个Copilot License" / "Copilot License" → 改为更通用表述
- "Cursor + Agentic Coding"（chapter4 里的示例表格，具体工具名保留）
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# 每个文件的精确替换规则
# (filepath_relative, [(old, new), ...])
# ============================================================
FILE_RULES = {
    # ---- KIM Doc Markdown ----
    'ai-transformation-kim-doc.md': [
        (
            '# 01 问题根源：为什么"买了Cursor全员推"不管用',
            '# 01 问题根源：为什么"买了 Cursor / Manus / OpenClaw 等AI工具全员推"不管用',
        ),
        (
            '| **AI工具普及** | 采购Cursor/Copilot，发邮件通知 | 用不用全靠自觉 |',
            '| **AI工具普及** | 采购 Cursor / Manus / OpenClaw 等AI工具，发邮件通知 | 用不用全靠自觉 |',
        ),
    ],

    # ---- 配图 HTML（需重新截图）----
    'images/gen/ch01-problem.html': [
        (
            '为什么"买了Cursor全员推"不管用？',
            '为什么"买了 Cursor / Manus / OpenClaw 等AI工具全员推"不管用？',
        ),
    ],

    # ---- chapter1.html ----
    'chapters/chapter1.html': [
        (
            '<!-- 第一章：为什么"买了Cursor全员推"不管用 -->',
            '<!-- 第一章：为什么"买了AI工具（Cursor/Manus/OpenClaw等）全员推"不管用 -->',
        ),
        (
            '<text x="65" y="55" text-anchor="middle" font-size="11" fill="#78716C">买Cursor/Copilot</text>',
            '<text x="65" y="55" text-anchor="middle" font-size="11" fill="#78716C">买AI工具(Cursor等)</text>',
        ),
        (
            '很多公司买了Cursor、配了Copilot，但最终只有少数"高手"在用，大部分人要么不会用，要么懒得用，要么用了也没感觉。',
            '很多公司买了 Cursor、Manus、OpenClaw 等AI工具，但最终只有少数"高手"在用，大部分人要么不会用，要么懒得用，要么用了也没感觉。',
        ),
        (
            '采购Cursor/Copilot，发邮件通知',
            '采购 Cursor / Manus / OpenClaw 等AI工具，发邮件通知',
        ),
        (
            '<span class="chapter-nav-name">为什么不管用</span>',
            '<span class="chapter-nav-name">为什么"买了AI工具全员推"不管用</span>',
        ),
    ],

    # ---- chapter2.html ----
    'chapters/chapter2.html': [
        (
            '今天企业买了Cursor全员推，大多数人也只是"写代码时让AI补全一下"——本质上和"用智能手机打电话"一样。',
            '今天企业买了 Cursor / Manus / OpenClaw 等AI工具全员推，大多数人也只是"用AI补全一下"——本质上和"用智能手机打电话"一样。',
        ),
        (
            '<span class="chapter-nav-name">为什么"买了Cursor全员推"不管用</span>',
            '<span class="chapter-nav-name">为什么"买了AI工具全员推"不管用</span>',
        ),
    ],

    # ---- chapter3.html ----
    'chapters/chapter3.html': [
        (
            '正在从"给每个人发一个Copilot License"升级为构建',
            '正在从"给每个人发一个AI工具License"升级为构建',
        ),
    ],

    # ---- chapter6.html ----
    'chapters/chapter6.html': [
        (
            '带着四阶段视角，重新审视"买了Cursor全员推"的本质问题',
            '带着四阶段视角，重新审视"买了AI工具全员推"的本质问题',
        ),
    ],

    # ---- index-full.html ----
    'index-full.html': [
        (
            '<!-- 第一章：为什么"买了Cursor全员推"不管用 -->',
            '<!-- 第一章：为什么"买了AI工具（Cursor/Manus/OpenClaw等）全员推"不管用 -->',
        ),
        (
            '<text x="65" y="48" text-anchor="middle" font-size="10" fill="#78716C">买Cursor/Copilot</text>',
            '<text x="65" y="48" text-anchor="middle" font-size="10" fill="#78716C">买AI工具(Cursor等)</text>',
        ),
        (
            '很多公司买了Cursor、配了Copilot，但最终只有少数"高手"在用，大部分人要么不会用，要么懒得用，要么用了也没感觉。',
            '很多公司买了 Cursor、Manus、OpenClaw 等AI工具，但最终只有少数"高手"在用，大部分人要么不会用，要么懒得用，要么用了也没感觉。',
        ),
        (
            '采购Cursor/Copilot，发邮件通知',
            '采购 Cursor / Manus / OpenClaw 等AI工具，发邮件通知',
        ),
        (
            '今天企业买了Cursor全员推，大多数人也只是"写代码时让AI补全一下"——本质上和"用智能手机打电话"一样。',
            '今天企业买了 Cursor / Manus / OpenClaw 等AI工具全员推，大多数人也只是"用AI补全一下"——本质上和"用智能手机打电话"一样。',
        ),
        (
            '正在从"给每个人发一个Copilot License"升级为构建',
            '正在从"给每个人发一个AI工具License"升级为构建',
        ),
        (
            '带着四阶段视角，重新审视"买了Cursor全员推"的本质问题',
            '带着四阶段视角，重新审视"买了AI工具全员推"的本质问题',
        ),
    ],

    # ---- full-report.html ----
    'full-report.html': [
        (
            '<!-- 第一章：为什么"买了Cursor全员推"不管用 -->',
            '<!-- 第一章：为什么"买了AI工具（Cursor/Manus/OpenClaw等）全员推"不管用 -->',
        ),
        (
            '<text x="65" y="48" text-anchor="middle" font-size="10" fill="#78716C">买Cursor/Copilot</text>',
            '<text x="65" y="48" text-anchor="middle" font-size="10" fill="#78716C">买AI工具(Cursor等)</text>',
        ),
        (
            '很多公司买了Cursor、配了Copilot，但最终只有少数"高手"在用，大部分人要么不会用，要么懒得用，要么用了也没感觉。',
            '很多公司买了 Cursor、Manus、OpenClaw 等AI工具，但最终只有少数"高手"在用，大部分人要么不会用，要么懒得用，要么用了也没感觉。',
        ),
        (
            '采购Cursor/Copilot，发邮件通知',
            '采购 Cursor / Manus / OpenClaw 等AI工具，发邮件通知',
        ),
        (
            '今天企业买了Cursor全员推，大多数人也只是"写代码时让AI补全一下"——本质上和"用智能手机打电话"一样。',
            '今天企业买了 Cursor / Manus / OpenClaw 等AI工具全员推，大多数人也只是"用AI补全一下"——本质上和"用智能手机打电话"一样。',
        ),
        (
            '<span class="chapter-nav-name">为什么"买了Cursor全员推"不管用</span>',
            '<span class="chapter-nav-name">为什么"买了AI工具全员推"不管用</span>',
        ),
        (
            '正在从"给每个人发一个Copilot License"升级为构建',
            '正在从"给每个人发一个AI工具License"升级为构建',
        ),
        (
            '带着四阶段视角，重新审视"买了Cursor全员推"的本质问题',
            '带着四阶段视角，重新审视"买了AI工具全员推"的本质问题',
        ),
    ],
}

def main():
    print('=== 批量修改 Cursor/Copilot 工具名 ===\n')
    total_modified = 0

    for rel_path, rules in FILE_RULES.items():
        abs_path = os.path.join(BASE, rel_path)
        if not os.path.exists(abs_path):
            print(f'⚠️  文件不存在: {rel_path}')
            continue

        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        changes = []
        for old, new in rules:
            if old in content:
                count = content.count(old)
                content = content.replace(old, new)
                changes.append(f'  [{count}处] {repr(old[:60])}')
            else:
                changes.append(f'  [未找到] {repr(old[:60])}')

        if content != original:
            with open(abs_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'✅ {rel_path}')
            for c in changes:
                print(c)
            total_modified += 1
        else:
            print(f'⏭  无变化: {rel_path}')

    print(f'\n共修改 {total_modified} 个文件')

    # ---- 最终验证：确认不再含有旧文字 ----
    print('\n=== 最终验证 ===')
    CHECK_PATTERNS = [
        '买了Cursor全员推',
        '采购Cursor/Copilot，发邮件通知',
        '买了Cursor、配了Copilot',
        '<span class="chapter-nav-name">为什么"买了Cursor全员推"不管用</span>',
    ]
    SKIP_PATTERNS = [
        'Data Copilot',       # 阿里云产品名，不改
        'Cursor + Agentic',   # 工具示例，不改
    ]
    all_pass = True
    for rel_path in FILE_RULES.keys():
        abs_path = os.path.join(BASE, rel_path)
        if not os.path.exists(abs_path):
            continue
        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read()
        for pat in CHECK_PATTERNS:
            if pat in content:
                print(f'  ❌ 仍存在旧文字 [{pat}] 在 {rel_path}')
                all_pass = False
    if all_pass:
        print('  ✅ 所有旧文字已清除')

if __name__ == '__main__':
    main()
