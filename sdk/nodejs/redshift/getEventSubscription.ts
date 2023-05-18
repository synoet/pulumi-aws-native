// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.
 */
export function getEventSubscription(args: GetEventSubscriptionArgs, opts?: pulumi.InvokeOptions): Promise<GetEventSubscriptionResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:redshift:getEventSubscription", {
        "subscriptionName": args.subscriptionName,
    }, opts);
}

export interface GetEventSubscriptionArgs {
    /**
     * The name of the Amazon Redshift event notification subscription
     */
    subscriptionName: string;
}

export interface GetEventSubscriptionResult {
    /**
     * The name of the Amazon Redshift event notification subscription.
     */
    readonly custSubscriptionId?: string;
    /**
     * The AWS account associated with the Amazon Redshift event notification subscription.
     */
    readonly customerAwsId?: string;
    /**
     * A boolean value; set to true to activate the subscription, and set to false to create the subscription but not activate it.
     */
    readonly enabled?: boolean;
    /**
     * Specifies the Amazon Redshift event categories to be published by the event notification subscription.
     */
    readonly eventCategories?: enums.redshift.EventSubscriptionEventCategoriesItem[];
    /**
     * The list of Amazon Redshift event categories specified in the event notification subscription.
     */
    readonly eventCategoriesList?: string[];
    /**
     * Specifies the Amazon Redshift event severity to be published by the event notification subscription.
     */
    readonly severity?: enums.redshift.EventSubscriptionSeverity;
    /**
     * The Amazon Resource Name (ARN) of the Amazon SNS topic used to transmit the event notifications.
     */
    readonly snsTopicArn?: string;
    /**
     * A list of one or more identifiers of Amazon Redshift source objects.
     */
    readonly sourceIds?: string[];
    /**
     * A list of the sources that publish events to the Amazon Redshift event notification subscription.
     */
    readonly sourceIdsList?: string[];
    /**
     * The type of source that will be generating the events.
     */
    readonly sourceType?: enums.redshift.EventSubscriptionSourceType;
    /**
     * The status of the Amazon Redshift event notification subscription.
     */
    readonly status?: enums.redshift.EventSubscriptionStatus;
    /**
     * The date and time the Amazon Redshift event notification subscription was created.
     */
    readonly subscriptionCreationTime?: string;
}
/**
 * The `AWS::Redshift::EventSubscription` resource creates an Amazon Redshift Event Subscription.
 */
export function getEventSubscriptionOutput(args: GetEventSubscriptionOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetEventSubscriptionResult> {
    return pulumi.output(args).apply((a: any) => getEventSubscription(a, opts))
}

export interface GetEventSubscriptionOutputArgs {
    /**
     * The name of the Amazon Redshift event notification subscription
     */
    subscriptionName: pulumi.Input<string>;
}
