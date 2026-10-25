# TMC Skills

面向 **IEEE Transactions on Mobile Computing（TMC）** 的科研技能包。沿用旧 TWC 包的九模块划分，重新编写 TMC 的领域判断、建模、实验与证据规则。每个 `skills/tmc-*` 文件夹都是可单独使用的 skill，包含自己的引用文件，不依赖兄弟模块。

本包依据用户提供的 **36 篇论文、568 个 PDF 页面**制作：全部做元数据/结构清点，并针对典型方法、实验页面和图表进行重点阅读。样本主要来自联邦学习与边缘计算，不能代表 TMC 全部方向；没有声称逐页审阅全部论文或验证全部证明。语料归纳与期刊正式要求已明确分开。

## 选择模块

| Skill | 用途 |
|---|---|
| [tmc-reader](skills/tmc-reader/SKILL.md) | 阅读、解读及按需制作全文中英对照 |
| [tmc-writing](skills/tmc-writing/SKILL.md) | 论文写作、系统建模、理论分析、实验与自查 |
| [tmc-polishing](skills/tmc-polishing/SKILL.md) | 英文学术润色与中文草稿翻译 |
| [tmc-figure](skills/tmc-figure/SKILL.md) | 真实数据绘图、系统图、图注及图表审查 |
| [tmc-response](skills/tmc-response/SKILL.md) | 逐点回复、修改矩阵及正文一致性审查 |
| [tmc-academic-search](skills/tmc-academic-search/SKILL.md) | 文献检索、综述与基线发现 |
| [tmc-citation](skills/tmc-citation/SKILL.md) | 引文核验、句子支撑匹配与参考文献导出 |
| [tmc-data](skills/tmc-data/SKILL.md) | 数据与代码可用性声明、复现材料检查 |
| [tmc-paper2ppt](skills/tmc-paper2ppt/SKILL.md) | 论文转 PPT、组会汇报与讲稿 |

## 使用

按任务阅读对应 `SKILL.md`；如果你的工具已经支持自定义 skills，把需要的**整个** `skills/tmc-*` 文件夹复制到其 skills 目录，保留 `references/`、`scripts/` 和 `agents/`。也可以让支持本地文件的代理直接读取对应入口。本次只制作文件，没有修改任何已安装 skill 或全局配置。

示例请求：

- “使用 $tmc-writing，根据这些方法和结果重写 Introduction，保留未完成实验的缺口。”
- “使用 $tmc-reader，解释这篇论文的系统模型和式 (7)，标出原文位置。”
- “使用 $tmc-response，按审稿意见和实际修改记录写逐点回复。”
- “使用 $tmc-figure，根据这些 CSV 数据绘制时间—准确率曲线。”
- “使用 $tmc-citation，核验这些句子的文献支撑，并导出 BibTeX。”

自动选择所需技能保持默认启用。Claude 风格插件清单位于 `.claude-plugin/plugin.json`；它仅是本地包描述，本包没有创建远程仓库、市场发布或网络服务。具体加载方式以使用工具的当前说明为准。

## TMC 适配内容

- 将论证重点落在移动/边缘系统的实际约束、机制、收益、代价和适用边界。
- 覆盖异步/半同步训练、异构资源、调度、拓扑、移动性、能耗/内存、隐私安全、LLM/LoRA 等相关检查；按研究问题选用，不要求每篇全部覆盖。
- 分清轮数与实际耗时、功率与能量、参数量与总通信量、仿真与实机、经验结果与理论保证。
- 审稿回复保留待办状态，不把计划补做写成已完成；引文核验分开检查书目信息和句子支撑。
- 移除旧包中遗留的 Nature/CNS/PubMed 默认范围、缺失脚本路径和与 TMC 无关的图像资产依赖。

## 语料依据

- [语料观察与逐篇索引](skills/tmc-writing/references/tmc-corpus-observations.md)
- [结构化清单：文件名、哈希、页数与检测候选](skills/tmc-writing/references/tmc-corpus-inventory.json)
- [官方来源与适用边界](skills/tmc-writing/references/tmc-context.md)

不包含原始论文 PDF、全文翻译、整篇抽取文本或论文图片。参考文件中的文章页码为 PDF 的一基页码。官方 TMC 范围和 IEEE 可复现性来源核对日期为 **2026-10-25**；页数限制、费用、匿名规则、补充材料规则等未写死，使用时查当期官方要求。

## 可运行工具与校验

本次实际检查结果见 [制作与验证记录](VALIDATION.md)。

需要 Python 3.10+。只读资料和技能本身不要求启动服务或配置密钥。

| 工具 | 作用 | 额外依赖 |
|---|---|---|
| [analyze_tmc_corpus.py](scripts/analyze_tmc_corpus.py) | 重建目录内 PDF 结构化清单，不导出论文全文 | PyMuPDF |
| [plot_results.py](skills/tmc-figure/scripts/plot_results.py) | 对真实 CSV 绘制均值曲线及可选样本标准差，导出 PDF/SVG/PNG/汇总 CSV | matplotlib |
| [export_references.py](skills/tmc-citation/scripts/export_references.py) | 把已核验 JSON 书目信息导出 BibTeX/RIS/EndNote；不联网、不代替内容核验 | Python 标准库 |
| [validate_bundle.py](scripts/validate_bundle.py) | 检查入口、YAML、内部链接、独立可用性与清单一致性 | PyYAML |

所有工具支持 `--help`（校验脚本接受可选包路径），默认拒绝覆盖现有结果；图表工具不生成实验数据。完整 JSON/CSV 输入约定见对应模块参考文件。

维护时，从本包根目录运行：

```text
python -B scripts/validate_bundle.py
python -B -m unittest discover -s tests -v
python -B scripts/analyze_tmc_corpus.py /path/to/papers --output new-inventory.json
```

结构化清单重建不会自动更新人工阅读观察；新增论文需要重新检查内容和页码。测试使用明确标记的合成数据，不作为论文证据。

## 来源与许可

参考用户提供的 `TWC-skills-main.zip`（其说明指出源自 nature-skills 框架）进行重新设计。保留原包 MIT [许可证](LICENSE)及原版权信息。新增说明、脚本与配置随此包采用同一许可；用户提供论文的版权不受该软件许可影响。未复制旧包的医学/生物图片、外部联网服务、个人邮箱或失效命令。
