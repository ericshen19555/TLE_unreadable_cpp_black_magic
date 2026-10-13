ENCODING = "utf-8"

prefix = r"""\documentclass[10pt, a4paper, twocolumn]{article}

% --- 基本設定 ---
\usepackage{geometry}
\geometry{a4paper, top=1.8cm, bottom=0.5cm, left=0.5cm, right=0.5cm}

% --- 中文支援 ---
\usepackage{xeCJK}
\setCJKmainfont{Noto Serif TC} % 可替換為其他字型，如 Microsoft JhengHei 或 PingFang TC

% --- 數學與符號 ---
\usepackage{amsmath}

% 支援刪除線
\usepackage[normalem]{ulem}

% 段落縮排
\usepackage{indentfirst}
\setlength{\parindent}{2em} 
% 行距調整
\usepackage{setspace}

% --- 預設內文樣式 ---
\setstretch{1.3}
\setlength{\parskip}{0.6em}

% --- 定義還原樣式（單行距 + 無段距） ---
\newcommand{\normaltextspacing}{%
	\setstretch{1.0}%
	\setlength{\parskip}{0pt}%
}
\newcommand{\resumetextspacing}{%
	\setstretch{1.3}%
	\setlength{\parskip}{0.6em}%
}

% --- 進入這些區塊時暫時關閉文字樣式 ---
\BeforeBeginEnvironment{itemize}{\normaltextspacing}
\AfterEndEnvironment{itemize}{\resumetextspacing}

\BeforeBeginEnvironment{enumerate}{\normaltextspacing}
\AfterEndEnvironment{enumerate}{\resumetextspacing}

\BeforeBeginEnvironment{minted}{\normaltextspacing}
\AfterEndEnvironment{minted}{\resumetextspacing}

% 表格行距
\renewcommand{\arraystretch}{1.5}

% 自訂 quote
\usepackage[most]{tcolorbox}
\usepackage{xcolor}

\renewenvironment{quote}
{\begin{tcolorbox}[
		colback=white,
		colframe=gray,
		left=4mm,
		right=0mm,
		top=2mm,
		bottom=2mm,
		boxrule=-1pt,
		enhanced,
		borderline west={1.5pt}{0pt}{gray},
		sharp corners,
		before skip=8pt, after skip=8pt,
		boxsep=2pt,
		breakable, 
		fontupper=\color{gray}
		]}
	{\end{tcolorbox}}

\usepackage{minted}
\setminted{
	fontsize=\small,
	frame=lines,   % 加上外框
	breaklines     % 自動換行
}

% --- 圖片與超連結 ---
\usepackage{graphicx}
\usepackage[hidelinks]{hyperref}
\usepackage{float} % 用於 [H] 強制圖片位置

% --- 標題與作者 ---
\title{TLE 的毒瘤高科技}
\author{暴力又被TLE}
\date{\today}

% --- 頁首頁尾設定 ---
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{} % 清除所有預設的頁首頁尾

% 使用 \makeatletter 以便存取 \@title 和 \@author 內部變數
\makeatletter
\lhead{\@title} % 左邊頁首：文件標題
\rhead{\@author} % 右邊頁首：作者
\makeatother

\setlength{\headsep}{12pt} % 減少頁首與內文的間隔
\renewcommand{\headrulewidth}{0.4pt} % 頁首底下的分隔線粗細
\renewcommand{\footrulewidth}{0pt} % 移除頁尾分隔線 (若有)

% --- 縮小 section ---
\usepackage{titlesec}
% 格式: \titleformat{命令}[型態]{格式}{標號}{標號與文字間距}{標題內容前綴}
\titleformat{\section}
{\normalfont\large\bfseries}   % 樣式 (這裡把 section 改小成 large)
{\thesection}                  % 顯示章節號
{1em}                          % 章節號和文字之間的距離
{}                             % 標題內容的前綴 (這裡留空)

% 格式: \titlespacing{命令}{左邊縮排}{與前段距離}{與後段距離}
\titlespacing{\section}
{0pt}      % 左縮排
{6pt plus 2pt minus 2pt}    % 前段距離 (預設大約 12pt~20pt)
{6pt plus 2pt minus 2pt}    % 後段距離 (預設大約 6pt~12pt)


\renewcommand{\contentsname}{目錄}

\begin{document}
	
	\tableofcontents
	\newpage
	
"""
suffix = r"""
\end{document}
"""

file_name = "競程模板"

with open(f"{file_name}.md", "r", encoding=ENCODING) as file:
    md_lines = file.readlines()

in_code = False
output = []
for line in md_lines:
    if in_code:
        if line.startswith("```"):
            in_code = False
            output.append("\\end{minted}\n")
        else:
            output.append(line)
    else:
        if line.startswith("```"):
            in_code = True
            language = line.lstrip("```").rstrip()
            language = "".join(c for c in language if c.isalpha())
            if language:
                output.append(f"\\begin{{minted}}{{{language}}}\n")
            else:
                output.append(f"\\begin{{minted}}\n")
        elif line.startswith("# "):
            text = line.lstrip("# ").rstrip()
            output.append(f"\\section{{{text}}}\n")
        elif line.startswith("## "):
            text = line.lstrip("## ").rstrip()
            output.append(f"\\subsection{{{text}}}\n")
        elif line.strip():
            # output.append(f"{line.rstrip()} \\\\\n")
            output.append(line)
        else:
            output.append(line)

with open(f"{file_name}.tex", "w", encoding=ENCODING) as file:
    ...
    # file.write(prefix)
    # for line in output:
    #     file.write(line)
    # file.write(suffix)
