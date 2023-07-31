// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Amazon Lex conversational bot performing automated tasks such as ordering a pizza, booking a hotel, and so on.
 */
export function getBot(args: GetBotArgs, opts?: pulumi.InvokeOptions): Promise<GetBotResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:lex:getBot", {
        "id": args.id,
    }, opts);
}

export interface GetBotArgs {
    id: string;
}

export interface GetBotResult {
    readonly arn?: string;
    /**
     * Data privacy setting of the Bot.
     */
    readonly dataPrivacy?: outputs.lex.DataPrivacyProperties;
    readonly description?: string;
    readonly id?: string;
    /**
     * IdleSessionTTLInSeconds of the resource
     */
    readonly idleSessionTtlInSeconds?: number;
    readonly name?: string;
    readonly roleArn?: string;
    readonly testBotAliasSettings?: outputs.lex.BotTestBotAliasSettings;
}
/**
 * Amazon Lex conversational bot performing automated tasks such as ordering a pizza, booking a hotel, and so on.
 */
export function getBotOutput(args: GetBotOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetBotResult> {
    return pulumi.output(args).apply((a: any) => getBot(a, opts))
}

export interface GetBotOutputArgs {
    id: pulumi.Input<string>;
}
