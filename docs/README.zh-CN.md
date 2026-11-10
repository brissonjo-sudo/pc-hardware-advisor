<!-- language-bar -->
[English](../README.md) · [Français](README.fr.md) · [Español](README.es.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · **简体中文** · [日本語](README.ja.md) · [हिन्दी](README.hi.md) · [العربية](README.ar.md)
<!-- /language-bar -->

> **机器翻译，未经人工审校。** 以英文版 [../README.md](../README.md) 为准。欢迎提出修正意见，参见 [../CONTRIBUTING.md](../CONTRIBUTING.md)。

# PC Hardware Advisor

PC Hardware Advisor 是一个面向 Claude（Claude Code 以及 Claude 桌面应用中的 Cowork）的插件，使 Claude 在台式机硬件方面更加可靠。它可以查找任何地区某个配件的最佳到手价，检查配件之间是否兼容，针对用途和预算设计完整配置单，为本地 AI 选配机器，评估二手商品信息，并按计划监控价格。插件给出的每个数字都带有日期、来源和置信度等级。插件只做读取：它从不购买任何东西，也从不联系卖家。

Claude 使用你书写所用的语言回答。配件名称、SKU 和单位保持原样。

## 功能说明

六项技能和一个子代理。

- **`hunt-prices`**：为一件确切的商品在全球范围内查找最佳到手价（含配送、增值税、关税和运费）。直营零售商优先，第三方市场单独列出，每一行都有置信度一栏。它会调用 `price-scout` 代理并行读取多个网站。
- **`check-compatibility`**：给出配件两两之间的判定：兼容、有条件兼容或不兼容。有条件的判定会写明确切条件及其来源。
- **`build-config`**：根据用途、预算、所在国家和你的约束设计完整配置单。它会给出一套主配置，以及一套更便宜和一套性能更强的变体。它只推荐新品和专业翻新的配件。
- **`size-local-ai`**：为本地运行模型估算硬件需求。涵盖显存、显存带宽、每秒词元数估算（均标注为估算）、多显卡、APU、外接显卡（eGPU）以及软件环境。
- **`review-used-listing`**：评估一条二手商品信息，并给出结论：下单、议价或放弃。它会提供给卖家的问题、交接时要做的测试，以及议价空间。
- **`track-price`**：设置价格的定时复查，只在价格低于你的阈值时提醒，并保存历史记录文件。它从不购买。
- **`price-scout`**（代理）：读取多个零售商或市场页面上某件确切配件的信息，返回标准化的价格行，不做分析。`hunt-prices` 会启动它。

超出范围：游戏主机、智能手机、平板电脑、作为产品的笔记本电脑，以及任何购买商品或联系卖家的操作。

## 原则

- **每个价格都有日期。** 没有读取日期的价格不予报告。
- **卖家类型明确标注。** 直营零售商、第三方市场卖家、翻新商和个人卖家是不同的行，绝不混在一起。
- **到手价，或“不含费用”。** 价格包含增值税、关税以及运至你所在国家的运费。当某项费用无法确定时，该行会写“不含费用”，而不是随意猜测。
- **置信度可见。** 每个数字都会说明其依据的充分程度。
- **绝不编造。** 如果某项参数、价格或规则无法找到来源，Claude 会直接说明。
- **被屏蔽的网站：改用浏览器，绝不取巧。** 如果某个网站拒绝自动读取，且有可用的浏览器工具，Claude 会用一行字询问是否在你的浏览器中打开该页面；回复“是”后，它会以只读方式阅读少数关键页面，并予以说明。遇到验证码或机器人检测时它会停止，绝不冒充真人来通过。否则，它会请你提供截图或粘贴的文本。不使用替代用户代理、缓存或镜像。
- **只读。** 插件从不购买、从不注册账户、从不提交表单、从不联系卖家。这些操作由你自己完成。

十份共享参考资料（研究方法、各国零售商、零售商评判标准、跨境购买、二手市场检查清单、插槽与芯片组、内存、电源与接口、板型与机箱、用于 AI 的显卡带宽）均注明了日期和来源。最近一次核对日期为 2026-11-07。

## 安装

### Claude Code

将本仓库用作插件市场，然后从中安装插件。

```
claude plugin marketplace add <owner/repo or local path>
claude plugin install pc-hardware-advisor@pc-hardware-advisor
```

`marketplace add` 接受 GitHub 仓库（`owner/repo`）、git 或 https 地址，或本地路径。对于本仓库，GitHub 地址为 `brissonjo-sudo/pc-hardware-advisor`。如果不想进行用户级安装（默认为 `user`），可以在上述任一命令后添加 `--scope project` 或 `--scope local`。

使用 `claude plugin marketplace list` 查看已安装的内容。

### 本地开发

若要在工作副本中试用插件而不安装：

```
claude --plugin-dir <path to this repository>
```

### Claude 桌面应用 / Cowork

获取 `pc-hardware-advisor.plugin` 文件（发布版本时会附在发行版中；也可以用工作副本通过 `python scripts/build_plugin.py` 构建，输出到 `dist/` 目录），将其拖入 Claude 桌面应用，然后接受安装提示。

### OpenAI Codex(实验性)

本仓库也是一个 Codex 插件市场(`.agents/plugins/marketplace.json`,清单 `.codex-plugin/plugin.json`)。添加后,从 ChatGPT 桌面应用或 Codex(`/plugins`)的插件目录安装插件:

```
codex plugin marketplace add brissonjo-sudo/pc-hardware-advisor
```

尚未测试。Codex 没有子代理:价格页面逐个读取,速度较慢。定时价格跟踪需要会话中有调度工具。仓库为私有:该命令需要对仓库的 git 访问权限。

## 更新、验证与卸载

**更新（Claude Code）。** 先刷新 marketplace，再更新插件，然后重启 Claude Code：

```
claude plugin marketplace update pc-hardware-advisor
claude plugin update pc-hardware-advisor@pc-hardware-advisor
```

只有当 `plugin.json` 中的 `version` 发生变化时，才会提示更新。

**验证。** 向 Claude 提问“你有哪些 PC 硬件相关的插件 skill？”，或运行 `claude plugin list`，查看是否有 `pc-hardware-advisor` 及其版本。

**卸载。** 运行 `claude plugin uninstall pc-hardware-advisor@pc-hardware-advisor`。在 Claude 桌面应用中，请在插件设置里移除该插件。你创建的价格历史文件仍保留在你存放的位置。

该仓库目前为私有，因此 marketplace 方式仅适用于有访问权限的账号；`.plugin` 文件是替代方案。

## 请求示例

Claude 会根据请求自动选择合适的技能。以下是几个例子：

1. “查找 Ryzen 7 9800X3D 送到德国的最佳到手价。直营零售商优先，第三方市场单独列出。”
2. “把 RTX 5070 Ti 从美国进口到加拿大，算上关税和运费，是否更便宜？”
3. “这套 DDR5-6000 内存能配 ASUS TUF B650 主板和 Ryzen 7 7700 吗？每一对配件分别给出判定。”
4. “在西班牙为我配一台 1,400 欧元的安静型 1440p 游戏电脑。也给我一套更便宜和一套性能更强的变体。”
5. “我想在本地以可用的速度运行 70B 模型。需要多大的显存和内存带宽？两块二手 24 GB 显卡够用吗？”
6. “帮我看看这条二手 RTX 3090 商品信息（链接见下）。下单、议价还是放弃？我应该问卖家什么？”
7. “监控英国市场上三星 990 Pro 2 TB 的价格，只有低于 120 英镑时才提醒我。”
8. 法语：“Trouve-moi le meilleur prix livré en France pour une alimentation 850 W ATX 3.1, vendeurs directs d'abord, places de marché à part.”（帮我找法国送货到家的最佳价格，一台 850 W ATX 3.1 电源，直营卖家优先，第三方市场单列。）
9. 西班牙语：“Quiero montar un PC para edición de vídeo con 1.800 EUR en España. ¿Qué configuración me recomiendas, y qué compatibilidad debo vigilar entre placa, RAM y GPU?”（我想在西班牙花 1,800 欧元组装一台用于视频剪辑的电脑。你推荐什么配置？主板、内存和显卡之间需要注意哪些兼容性？）
10. “拥有 64 GB 统一内存的 APU 能运行 32B 模型吗？我该期望什么速度？请标明哪些是估算。”

## 连接器

技能按类别（网页搜索、网页抓取、价格比较工具、分类信息网站、浏览器、调度器、通知）而非具体产品来引用工具，因此任何等效工具都可以使用。插件的任何部分都不需要账户、API 密钥或付费服务。类别、可选数据源以及适用于所有工具的规则，详见 [CONNECTORS.md](../CONNECTORS.md)。

## 局限

- **价格有时效性。** 价格仅在其读取日期时有效。库存和促销活动可能在数小时内变化。
- **部分网站屏蔽自动读取。** 这些行会被标记为被屏蔽，Claude 会请你提供截图或粘贴的文本。
- **税收和关税规则变动频繁。** 增值税、海关关税和免税起征额在 2025 年和 2026 年多次变化。进行大额进口前，请查阅官方来源。
- **估算终究是估算。** 每秒词元数等数值及类似的预测是基于模型推算的，并非在你的机器上实测，且均有相应标注。
- **研究覆盖存在空白。** 部分国家、零售商和小众配件的覆盖较为薄弱。参考资料中会注明具体情况。
- **请使用高推理强度（effort）。** 在维护者的测试中，中等强度下的 `build-config` 读取的零售商更少，并错过了更便宜的选项。在请求配置或比价之前，请在应用中选择高强度。
- **不构成财务或法律建议。** 插件仅为购买决策提供参考，不提供税务、海关或消费者法方面的建议。

## 隐私

插件本身不收集任何信息，也不向任何地方发送数据。`track-price` 写入的价格历史保存在你选择的位置。Claude 用于搜索和读取网页的工具（网页搜索、网页抓取、调度器）遵循各自提供方的服务条款和隐私政策。

## 翻译

以下为本 README 的机器翻译版本，未经人工审校：[README.fr.md](README.fr.md)、[README.es.md](README.es.md)、[README.zh-CN.md](README.zh-CN.md)、[README.hi.md](README.hi.md)、[README.pt.md](README.pt.md)、[README.ar.md](README.ar.md)、[README.de.md](README.de.md)、[README.ja.md](README.ja.md)。以英文版为准。

## 参与贡献

欢迎贡献，但须遵守特定条款，包括权利转让。在提交 pull request 之前，请先阅读 [CONTRIBUTING.md](../CONTRIBUTING.md)。

## 许可证

PC Hardware Advisor 以 PolyForm Noncommercial License 1.0.0（SPDX：PolyForm-Noncommercial-1.0.0）授权，源代码可获取。任何人都可以出于非商业目的使用；商业使用需要向作者另行取得许可。同一许可证也适用于技能、参考资料、文档和翻译。

完整文本：[LICENSE](../LICENSE)，以及 <https://polyformproject.org/licenses/noncommercial/1.0.0>。
