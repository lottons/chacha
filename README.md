# chacha

## 目标

通过分析安卓应用市场的应用数据，并进行分析后，提供应用、游戏的最新趋势，并通过数据挖掘分析推荐有趣的、好玩的应用和游戏。

### 架构

总体上主要分成两大部分：

1. 网络数据抓取部分

网络数据抓取，借助于Python实现。通过爬取应用市场的网页数据，并对数据进行保存处理。

主要包括以下模块：

- spider_main 主入口，提供定时拉起任务的能力；

- html_downer html页面的下载器，用于向指定的url读取html页面；

- parser 解析器，在html_downer下载页面后，用于解析html页面，获取有用的数据信息。parser不是根据固定的html页面内容来进行解析，该parser可以根据配置文件指定的格式来获取相应的数据。

parser针对需要解析的内容，支持配置化的数据信息的分析和抓取。

当前，parser可以针对以下的页面进行配置化的解析处理：

- [x] 排行信息的页面，适用于在一个页面上有应用排行、游戏排行、最新上架、上升最快等排行的信息；

- [x] 单一排行信息的页面，适用于在一个页面上行只展示某一个独立分类的排行的页面；

- [ ] 专题信息的页面，按照不同的专题进行分类的页面信息；

以上的的解析器，按照对应的分类提供独立的解析过程和对应的配置。每一个app应用市场，可以包含以上所有的解析器和对应的配置。

- output 数据输出器，用于将解析器分析得到的数据进行输出，当前主要提供以下数据输出器的实现：

- [x] 输出成txt文件，可以指定文件的格式（待实现）；

- [ ] 输出成csv文件；

- [ ] 输出到关系型数据库，如Mysql、PostgreSQL等。

对于文件类的输出，一个解析器可能输出的文件可能会是多个，因为一个解析器分析得到的数据会有多个分类。每一个分类的数据，会有输出器输出成对应的文件

2. 数据分析处理部分

这部分用于对数据抓取后的输出进行分析处理。
