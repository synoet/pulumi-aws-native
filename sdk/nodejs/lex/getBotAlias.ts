// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * A Bot Alias enables you to change the version of a bot without updating applications that use the bot
 */
export function getBotAlias(args: GetBotAliasArgs, opts?: pulumi.InvokeOptions): Promise<GetBotAliasResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:lex:getBotAlias", {
        "botAliasId": args.botAliasId,
        "botId": args.botId,
    }, opts);
}

export interface GetBotAliasArgs {
    botAliasId: string;
    botId: string;
}

export interface GetBotAliasResult {
    readonly arn?: string;
    readonly botAliasId?: string;
    readonly botAliasLocaleSettings?: outputs.lex.BotAliasLocaleSettingsItem[];
    readonly botAliasName?: string;
    readonly botAliasStatus?: enums.lex.BotAliasStatus;
    readonly botVersion?: string;
    readonly conversationLogSettings?: outputs.lex.BotAliasConversationLogSettings;
    readonly description?: string;
    /**
     * Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
     */
    readonly sentimentAnalysisSettings?: outputs.lex.SentimentAnalysisSettingsProperties;
}
/**
 * A Bot Alias enables you to change the version of a bot without updating applications that use the bot
 */
export function getBotAliasOutput(args: GetBotAliasOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetBotAliasResult> {
    return pulumi.output(args).apply((a: any) => getBotAlias(a, opts))
}

export interface GetBotAliasOutputArgs {
    botAliasId: pulumi.Input<string>;
    botId: pulumi.Input<string>;
}
