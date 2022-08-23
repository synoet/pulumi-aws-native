// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CodeStarNotifications::NotificationRule
 */
export function getNotificationRule(args: GetNotificationRuleArgs, opts?: pulumi.InvokeOptions): Promise<GetNotificationRuleResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:codestarnotifications:getNotificationRule", {
        "arn": args.arn,
    }, opts);
}

export interface GetNotificationRuleArgs {
    arn: string;
}

export interface GetNotificationRuleResult {
    readonly arn?: string;
    readonly createdBy?: string;
    readonly detailType?: enums.codestarnotifications.NotificationRuleDetailType;
    readonly eventTypeIds?: string[];
    readonly name?: string;
    readonly status?: enums.codestarnotifications.NotificationRuleStatus;
    readonly targets?: outputs.codestarnotifications.NotificationRuleTarget[];
}

export function getNotificationRuleOutput(args: GetNotificationRuleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetNotificationRuleResult> {
    return pulumi.output(args).apply(a => getNotificationRule(a, opts))
}

export interface GetNotificationRuleOutputArgs {
    arn: pulumi.Input<string>;
}
