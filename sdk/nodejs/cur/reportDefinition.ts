// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::CUR::ReportDefinition resource creates a Cost & Usage Report with user-defined settings. You can use this resource to define settings like time granularity (hourly, daily, monthly), file format (Parquet, CSV), and S3 bucket for delivery of these reports.
 *
 * @deprecated ReportDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class ReportDefinition extends pulumi.CustomResource {
    /**
     * Get an existing ReportDefinition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ReportDefinition {
        pulumi.log.warn("ReportDefinition is deprecated: ReportDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new ReportDefinition(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cur:ReportDefinition';

    /**
     * Returns true if the given object is an instance of ReportDefinition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ReportDefinition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ReportDefinition.__pulumiType;
    }

    /**
     * A list of manifests that you want Amazon Web Services to create for this report.
     */
    public readonly additionalArtifacts!: pulumi.Output<enums.cur.ReportDefinitionAdditionalArtifactsItem[] | undefined>;
    /**
     * A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs.
     */
    public readonly additionalSchemaElements!: pulumi.Output<enums.cur.ReportDefinitionAdditionalSchemaElementsItem[] | undefined>;
    /**
     * The Amazon resource name of the billing view. You can get this value by using the billing view service public APIs.
     */
    public readonly billingViewArn!: pulumi.Output<string | undefined>;
    /**
     * The compression format that AWS uses for the report.
     */
    public readonly compression!: pulumi.Output<enums.cur.ReportDefinitionCompression>;
    /**
     * The format that AWS saves the report in.
     */
    public readonly format!: pulumi.Output<enums.cur.ReportDefinitionFormat>;
    /**
     * Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.
     */
    public readonly refreshClosedReports!: pulumi.Output<boolean>;
    /**
     * The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.
     */
    public readonly reportName!: pulumi.Output<string>;
    /**
     * Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
     */
    public readonly reportVersioning!: pulumi.Output<enums.cur.ReportDefinitionReportVersioning>;
    /**
     * The S3 bucket where AWS delivers the report.
     */
    public readonly s3Bucket!: pulumi.Output<string>;
    /**
     * The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.
     */
    public readonly s3Prefix!: pulumi.Output<string>;
    /**
     * The region of the S3 bucket that AWS delivers the report into.
     */
    public readonly s3Region!: pulumi.Output<string>;
    /**
     * The granularity of the line items in the report.
     */
    public readonly timeUnit!: pulumi.Output<enums.cur.ReportDefinitionTimeUnit>;

    /**
     * Create a ReportDefinition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated ReportDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: ReportDefinitionArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("ReportDefinition is deprecated: ReportDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.compression === undefined) && !opts.urn) {
                throw new Error("Missing required property 'compression'");
            }
            if ((!args || args.format === undefined) && !opts.urn) {
                throw new Error("Missing required property 'format'");
            }
            if ((!args || args.refreshClosedReports === undefined) && !opts.urn) {
                throw new Error("Missing required property 'refreshClosedReports'");
            }
            if ((!args || args.reportName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'reportName'");
            }
            if ((!args || args.reportVersioning === undefined) && !opts.urn) {
                throw new Error("Missing required property 'reportVersioning'");
            }
            if ((!args || args.s3Bucket === undefined) && !opts.urn) {
                throw new Error("Missing required property 's3Bucket'");
            }
            if ((!args || args.s3Prefix === undefined) && !opts.urn) {
                throw new Error("Missing required property 's3Prefix'");
            }
            if ((!args || args.s3Region === undefined) && !opts.urn) {
                throw new Error("Missing required property 's3Region'");
            }
            if ((!args || args.timeUnit === undefined) && !opts.urn) {
                throw new Error("Missing required property 'timeUnit'");
            }
            resourceInputs["additionalArtifacts"] = args ? args.additionalArtifacts : undefined;
            resourceInputs["additionalSchemaElements"] = args ? args.additionalSchemaElements : undefined;
            resourceInputs["billingViewArn"] = args ? args.billingViewArn : undefined;
            resourceInputs["compression"] = args ? args.compression : undefined;
            resourceInputs["format"] = args ? args.format : undefined;
            resourceInputs["refreshClosedReports"] = args ? args.refreshClosedReports : undefined;
            resourceInputs["reportName"] = args ? args.reportName : undefined;
            resourceInputs["reportVersioning"] = args ? args.reportVersioning : undefined;
            resourceInputs["s3Bucket"] = args ? args.s3Bucket : undefined;
            resourceInputs["s3Prefix"] = args ? args.s3Prefix : undefined;
            resourceInputs["s3Region"] = args ? args.s3Region : undefined;
            resourceInputs["timeUnit"] = args ? args.timeUnit : undefined;
        } else {
            resourceInputs["additionalArtifacts"] = undefined /*out*/;
            resourceInputs["additionalSchemaElements"] = undefined /*out*/;
            resourceInputs["billingViewArn"] = undefined /*out*/;
            resourceInputs["compression"] = undefined /*out*/;
            resourceInputs["format"] = undefined /*out*/;
            resourceInputs["refreshClosedReports"] = undefined /*out*/;
            resourceInputs["reportName"] = undefined /*out*/;
            resourceInputs["reportVersioning"] = undefined /*out*/;
            resourceInputs["s3Bucket"] = undefined /*out*/;
            resourceInputs["s3Prefix"] = undefined /*out*/;
            resourceInputs["s3Region"] = undefined /*out*/;
            resourceInputs["timeUnit"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["additionalSchemaElements[*]", "billingViewArn", "reportName", "reportVersioning", "timeUnit"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ReportDefinition.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ReportDefinition resource.
 */
export interface ReportDefinitionArgs {
    /**
     * A list of manifests that you want Amazon Web Services to create for this report.
     */
    additionalArtifacts?: pulumi.Input<pulumi.Input<enums.cur.ReportDefinitionAdditionalArtifactsItem>[]>;
    /**
     * A list of strings that indicate additional content that Amazon Web Services includes in the report, such as individual resource IDs.
     */
    additionalSchemaElements?: pulumi.Input<pulumi.Input<enums.cur.ReportDefinitionAdditionalSchemaElementsItem>[]>;
    /**
     * The Amazon resource name of the billing view. You can get this value by using the billing view service public APIs.
     */
    billingViewArn?: pulumi.Input<string>;
    /**
     * The compression format that AWS uses for the report.
     */
    compression: pulumi.Input<enums.cur.ReportDefinitionCompression>;
    /**
     * The format that AWS saves the report in.
     */
    format: pulumi.Input<enums.cur.ReportDefinitionFormat>;
    /**
     * Whether you want Amazon Web Services to update your reports after they have been finalized if Amazon Web Services detects charges related to previous months. These charges can include refunds, credits, or support fees.
     */
    refreshClosedReports: pulumi.Input<boolean>;
    /**
     * The name of the report that you want to create. The name must be unique, is case sensitive, and can't include spaces.
     */
    reportName: pulumi.Input<string>;
    /**
     * Whether you want Amazon Web Services to overwrite the previous version of each report or to deliver the report in addition to the previous versions.
     */
    reportVersioning: pulumi.Input<enums.cur.ReportDefinitionReportVersioning>;
    /**
     * The S3 bucket where AWS delivers the report.
     */
    s3Bucket: pulumi.Input<string>;
    /**
     * The prefix that AWS adds to the report name when AWS delivers the report. Your prefix can't include spaces.
     */
    s3Prefix: pulumi.Input<string>;
    /**
     * The region of the S3 bucket that AWS delivers the report into.
     */
    s3Region: pulumi.Input<string>;
    /**
     * The granularity of the line items in the report.
     */
    timeUnit: pulumi.Input<enums.cur.ReportDefinitionTimeUnit>;
}
