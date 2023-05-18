// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Lightsail::Instance
 */
export function getInstance(args: GetInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:lightsail:getInstance", {
        "instanceName": args.instanceName,
    }, opts);
}

export interface GetInstanceArgs {
    /**
     * The names to use for your new Lightsail instance.
     */
    instanceName: string;
}

export interface GetInstanceResult {
    /**
     * An array of objects representing the add-ons to enable for the new instance.
     */
    readonly addOns?: outputs.lightsail.InstanceAddOn[];
    readonly hardware?: outputs.lightsail.InstanceHardware;
    readonly instanceArn?: string;
    /**
     * Is the IP Address of the Instance is the static IP
     */
    readonly isStaticIp?: boolean;
    /**
     * The name of your key pair.
     */
    readonly keyPairName?: string;
    readonly location?: outputs.lightsail.InstanceLocation;
    readonly networking?: outputs.lightsail.InstanceNetworking;
    /**
     * Private IP Address of the Instance
     */
    readonly privateIpAddress?: string;
    /**
     * Public IP Address of the Instance
     */
    readonly publicIpAddress?: string;
    /**
     * Resource type of Lightsail instance.
     */
    readonly resourceType?: string;
    /**
     * SSH Key Name of the  Lightsail instance.
     */
    readonly sshKeyName?: string;
    readonly state?: outputs.lightsail.InstanceState;
    /**
     * Support code to help identify any issues
     */
    readonly supportCode?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.lightsail.InstanceTag[];
    /**
     * Username of the  Lightsail instance.
     */
    readonly userName?: string;
}
/**
 * Resource Type definition for AWS::Lightsail::Instance
 */
export function getInstanceOutput(args: GetInstanceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstanceResult> {
    return pulumi.output(args).apply((a: any) => getInstance(a, opts))
}

export interface GetInstanceOutputArgs {
    /**
     * The names to use for your new Lightsail instance.
     */
    instanceName: pulumi.Input<string>;
}
