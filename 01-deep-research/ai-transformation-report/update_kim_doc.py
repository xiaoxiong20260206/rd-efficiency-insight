#!/usr/bin/env python3
"""
更新 ai-transformation-kim-doc.md：
1. 在文章最前面加 Web 版推荐横幅
2. 副标题同步最新版（含"趋势推演"）
3. # 01 章节补充 Web 版新增内容：
   - 1.5 智能手机类比（详细版表格）
   - 1.6 2026年全景数据
   - 1.7 趋势推演：未来18个月
   - 1.8 为什么跃迁如此困难（PwC 80/20法则详表）
"""
import re

with open('ai-transformation-kim-doc.md', 'r', encoding='utf-8') as f:
    content = f.read()

# ========== 1. 更新副标题（在文章 H1 标题之后）==========
old_subtitle = "**四阶段演进模型——从AI工具普及到业务AI化跃迁的本质规律、实操路径与度量体系**"
new_subtitle = "**四阶段演进模型——从AI工具普及到业务AI化跃迁的本质规律、实操路径、度量体系与趋势推演**"
content = content.replace(old_subtitle, new_subtitle)

# ========== 2. 在 H1 标题行上方插入 Web 版推荐横幅 ==========
web_banner = """> 🌐 **优先推荐阅读 Web 版本**：[AI组织转型深度调研报告（在线版）](https://xiaoxiong20260206.github.io/rd-efficiency-insight/01-deep-research/ai-transformation-report/index-full.html)
>
> Web 版支持**标签页导航**，可快速跳转各阶段；图表交互更佳，排版更清晰。本文档为同步镜像版本，供内网检索使用。

"""

# 在文件最开头（# AI组织转型深度调研 之前）插入
content = web_banner + content

# ========== 3. 在 # 01 章节末尾（--- 分隔线之前）插入新内容 ==========
# 定位：在"**智能手机类比**"所在行之后替换为完整版详细表格，
# 然后在 --- 前追加新增三个子章节

new_ch01_sections = """
## 1.5 智能手机类比：为什么跃迁节奏不可逆

| 智能手机时代 | AI转型对应 | 发生了什么 |
|------------|----------|---------|
| 人手一部智能机 | AI工具普及 | 大多数人只用来打电话、发微信——"新设备，旧用法" |
| 各工种深度使用 | 工种AI化重塑 | 摄影师用手机拍照修图、记者用手机现场写稿——每个工种被重新定义 |
| 一人拍+剪+发 | 团队AI化重组 | 以前做一条视频需要10人，现在1人完成——协作方式彻底重构，生产率飞跃在此 |
| 抖音/美团/移动支付 | 业务AI化跃迁 | 功能机时代不可能存在的全新业态 |

## 1.6 2026年全景：谁在哪个阶段

📌 **现状：74%的企业还没完成阶段一到阶段二的跃迁，真正进入阶段四的不到5%。**

| 占比 | 所在阶段 | 典型表现 |
|-----|---------|---------|
| **37%** | 停留在表面使用（阶段一：AI工具普及） | 买了工具，使用率不到20% |
| **30%** | 正在重设计关键流程（阶段二：工种AI化重塑） | 部分工种工作流有AI参与 |
| **34%** | 开始深度变革（阶段三探索） | 试点Pod团队 |
| **<5%** | 真正业务AI化跃迁（阶段四先锋） | AI原生收入已可见 |

> Deloitte 2026：员工AI工具使用率在2025年上升了50%，但企业在基础设施、数据质量、风险治理和人才储备方面的"准备度"反而**下降**了。

## 1.7 趋势推演：未来18个月将发生什么

| 趋势 | 2026上半年 | 2026下半年-2027 | 驱动力 |
|------|----------|---------------|------|
| GenAI从个人工具变为组织资源 | 头部企业建立"AI工厂/AI Studio" | 企业级AI平台成为标配 | MIT SMR：个人生产力增量"不可衡量" |
| Agentic AI从炒作进入落地 | 实际benchmark出现，落地案例增多 | 高价值工作流中Agent常态化 | PwC："Agent元年"可能到来 |
| "AI通才"取代专业分工 | PM覆盖范围扩大4-6倍 | 知识型劳动力呈"沙漏型" | BCG：职能边界消融 |
| 团队从金字塔变为扁平Pod | 先锋企业开始取消中间协调层 | 人+AI混合小团队成为主流 | BCG：4种组织原型浮现 |
| AI治理从可选变为必选 | 仅1/5企业有成熟Agent治理 | CAIO角色普及 | Deloitte：Agent速度超过治理能力 |

📌 **最关键预测**：2026年将是"阶段一到阶段二"的分水岭年。MIT SMR："If 2025 was the year of realizing that generative AI has a value-realization problem, 2026 will be the year of doing something about it."

## 1.8 为什么跃迁如此困难：PwC的80/20法则

每一级阶段跃迁难度呈**指数级**增长：技术只贡献20%的价值，**80%的价值来自工作方式的重新设计**。

| 跃迁 | 技术侧（20%） | 组织侧（80%） | 为什么卡住 |
|------|------------|------------|---------|
| 阶段1→2 | 工具已部署 | 需要重设计每个工种的工作流 | 个人习惯难改，缺乏最佳实践模板 |
| 阶段2→3 | 工作流已优化 | 需要重构团队协作模式和度量体系 | 组织惯性巨大，既得利益阻力 |
| 阶段3→4 | 团队已重组 | 需要重新定义"做什么"和"谁来做" | 需要CEO级别的战略决心 |

"""

# 将旧的"智能手机类比"一行替换成详细表格 + 新章节
old_analogy_line = "**智能手机类比**：人手一部智能机（AI工具普及）→ 各工种深度使用（工种重塑）→ 一人拍+剪+发（团队重组）→ 抖音/美团/移动支付诞生（业务跃迁）\n\n---\n"
new_analogy_replacement = new_ch01_sections + "\n---\n"

content = content.replace(old_analogy_line, new_analogy_replacement)

# ========== 4. 写回文件 ==========
with open('ai-transformation-kim-doc.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 更新完成！")
print("验证图片引用...")
import subprocess
result = subprocess.run(['grep', '-n', r'!\[', 'ai-transformation-kim-doc.md'], capture_output=True, text=True)
lines = [l for l in result.stdout.strip().split('\n') if l.strip()]
print(f"  图片引用总数: {len(lines)}")
backslash_result = subprocess.run(['grep', '-n', r'\\!\[', 'ai-transformation-kim-doc.md'], capture_output=True, text=True)
bad = [l for l in backslash_result.stdout.strip().split('\n') if l.strip()]
if bad:
    print(f"  ❌ 发现 \\![ 转义问题: {len(bad)} 处")
    for l in bad:
        print(f"    {l}")
else:
    print("  ✅ 无 \\![ 转义问题，图片语法正确")

# 检查 Web 横幅是否存在
if "优先推荐阅读 Web 版本" in content:
    print("  ✅ Web 版推荐横幅已插入")
else:
    print("  ❌ Web 版推荐横幅未找到")
    
# 检查新章节
for sec in ["1.5 智能手机类比", "1.6 2026年全景", "1.7 趋势推演", "1.8 为什么跃迁如此困难"]:
    if sec in content:
        print(f"  ✅ {sec} 已插入")
    else:
        print(f"  ❌ {sec} 未找到")
