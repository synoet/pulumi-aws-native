// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.
 */
export function getCertificateProvider(args: GetCertificateProviderArgs, opts?: pulumi.InvokeOptions): Promise<GetCertificateProviderResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iot:getCertificateProvider", {
        "certificateProviderName": args.certificateProviderName,
    }, opts);
}

export interface GetCertificateProviderArgs {
    certificateProviderName: string;
}

export interface GetCertificateProviderResult {
    readonly accountDefaultForOperations?: enums.iot.CertificateProviderOperation[];
    readonly arn?: string;
    readonly lambdaFunctionArn?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.iot.CertificateProviderTag[];
}
/**
 * Use the AWS::IoT::CertificateProvider resource to declare an AWS IoT Certificate Provider.
 */
export function getCertificateProviderOutput(args: GetCertificateProviderOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCertificateProviderResult> {
    return pulumi.output(args).apply((a: any) => getCertificateProvider(a, opts))
}

export interface GetCertificateProviderOutputArgs {
    certificateProviderName: pulumi.Input<string>;
}
