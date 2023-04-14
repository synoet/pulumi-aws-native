// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::Chatbot::SlackChannelConfiguration.
 */
export function getSlackChannelConfiguration(args: GetSlackChannelConfigurationArgs, opts?: pulumi.InvokeOptions): Promise<GetSlackChannelConfigurationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:chatbot:getSlackChannelConfiguration", {
        "arn": args.arn,
    }, opts);
}

export interface GetSlackChannelConfigurationArgs {
    /**
     * Amazon Resource Name (ARN) of the configuration
     */
    arn: string;
}

export interface GetSlackChannelConfigurationResult {
    /**
     * Amazon Resource Name (ARN) of the configuration
     */
    readonly arn?: string;
    /**
     * The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
     */
    readonly guardrailPolicies?: string[];
    /**
     * The ARN of the IAM role that defines the permissions for AWS Chatbot
     */
    readonly iamRoleArn?: string;
    /**
     * Specifies the logging level for this configuration:ERROR,INFO or NONE. This property affects the log entries pushed to Amazon CloudWatch logs
     */
    readonly loggingLevel?: string;
    /**
     * The id of the Slack channel
     */
    readonly slackChannelId?: string;
    /**
     * ARNs of SNS topics which delivers notifications to AWS Chatbot, for example CloudWatch alarm notifications.
     */
    readonly snsTopicArns?: string[];
    /**
     * Enables use of a user role requirement in your chat configuration
     */
    readonly userRoleRequired?: boolean;
}
/**
 * Resource schema for AWS::Chatbot::SlackChannelConfiguration.
 */
export function getSlackChannelConfigurationOutput(args: GetSlackChannelConfigurationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSlackChannelConfigurationResult> {
    return pulumi.output(args).apply((a: any) => getSlackChannelConfiguration(a, opts))
}

export interface GetSlackChannelConfigurationOutputArgs {
    /**
     * Amazon Resource Name (ARN) of the configuration
     */
    arn: pulumi.Input<string>;
}
