### Izzyagent

Customization for IzzyAgent

## LetterHead HTML Code:

Letter Head Based On : HTML

```
<table width="100%" style="width:100%; background-color: #ffffff; font-family: Arial, sans-serif; font-size: 14px; color: #333;">
    <tbody>
        <tr>
            <td width="40%">
                <img src="/assets/izzyagent/images/izzylogo.png" alt="IzzyAgent" style="margin-right: 10px;">
            </td>
            <td width="60%" style="text-align:left; padding-left:33% !important;">
                IzzyAgents Ltd <br>
                PO Box 301-288 <br>
                Albany 0752 <br>
                p: 09 415 7575 <br>
                e: accounts@izzybots.com <br>
                GST No : 131-907-605
            </td>
        </tr>
    </tbody>
</table>

```

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app izzyagent
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/izzyagent
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
