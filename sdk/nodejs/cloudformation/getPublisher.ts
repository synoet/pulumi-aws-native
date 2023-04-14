// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Register as a publisher in the CloudFormation Registry.
 */
export function getPublisher(args: GetPublisherArgs, opts?: pulumi.InvokeOptions): Promise<GetPublisherResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:cloudformation:getPublisher", {
        "publisherId": args.publisherId,
    }, opts);
}

export interface GetPublisherArgs {
    /**
     * The publisher id assigned by CloudFormation for publishing in this region.
     */
    publisherId: string;
}

export interface GetPublisherResult {
    /**
     * The type of account used as the identity provider when registering this publisher with CloudFormation.
     */
    readonly identityProvider?: enums.cloudformation.PublisherIdentityProvider;
    /**
     * The publisher id assigned by CloudFormation for publishing in this region.
     */
    readonly publisherId?: string;
    /**
     * The URL to the publisher's profile with the identity provider.
     */
    readonly publisherProfile?: string;
    /**
     * Whether the publisher is verified.
     */
    readonly publisherStatus?: enums.cloudformation.PublisherStatus;
}
/**
 * Register as a publisher in the CloudFormation Registry.
 */
export function getPublisherOutput(args: GetPublisherOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPublisherResult> {
    return pulumi.output(args).apply((a: any) => getPublisher(a, opts))
}

export interface GetPublisherOutputArgs {
    /**
     * The publisher id assigned by CloudFormation for publishing in this region.
     */
    publisherId: pulumi.Input<string>;
}
