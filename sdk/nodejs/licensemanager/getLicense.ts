// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::LicenseManager::License
 */
export function getLicense(args: GetLicenseArgs, opts?: pulumi.InvokeOptions): Promise<GetLicenseResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:licensemanager:getLicense", {
        "licenseArn": args.licenseArn,
    }, opts);
}

export interface GetLicenseArgs {
    /**
     * Amazon Resource Name is a unique name for each resource.
     */
    licenseArn: string;
}

export interface GetLicenseResult {
    /**
     * Beneficiary of the license.
     */
    readonly beneficiary?: string;
    readonly consumptionConfiguration?: outputs.licensemanager.LicenseConsumptionConfiguration;
    readonly entitlements?: outputs.licensemanager.LicenseEntitlement[];
    /**
     * Home region for the created license.
     */
    readonly homeRegion?: string;
    readonly issuer?: outputs.licensemanager.LicenseIssuerData;
    /**
     * Amazon Resource Name is a unique name for each resource.
     */
    readonly licenseArn?: string;
    readonly licenseMetadata?: outputs.licensemanager.LicenseMetadata[];
    /**
     * Name for the created license.
     */
    readonly licenseName?: string;
    /**
     * Product name for the created license.
     */
    readonly productName?: string;
    /**
     * ProductSKU of the license.
     */
    readonly productSKU?: string;
    readonly validity?: outputs.licensemanager.LicenseValidityDateFormat;
    /**
     * The version of the license.
     */
    readonly version?: string;
}
/**
 * Resource Type definition for AWS::LicenseManager::License
 */
export function getLicenseOutput(args: GetLicenseOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLicenseResult> {
    return pulumi.output(args).apply((a: any) => getLicense(a, opts))
}

export interface GetLicenseOutputArgs {
    /**
     * Amazon Resource Name is a unique name for each resource.
     */
    licenseArn: pulumi.Input<string>;
}
