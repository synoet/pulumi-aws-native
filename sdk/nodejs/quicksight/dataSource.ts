// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Definition of the AWS::QuickSight::DataSource Resource Type.
 */
export class DataSource extends pulumi.CustomResource {
    /**
     * Get an existing DataSource resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DataSource {
        return new DataSource(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:quicksight:DataSource';

    /**
     * Returns true if the given object is an instance of DataSource.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataSource {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataSource.__pulumiType;
    }

    /**
     * <p>A set of alternate data source parameters that you want to share for the credentials
     *             stored with this data source. The credentials are applied in tandem with the data source
     *             parameters when you copy a data source by using a create or update request. The API
     *             operation compares the <code>DataSourceParameters</code> structure that's in the request
     *             with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
     *             structures are an exact match, the request is allowed to use the credentials from this
     *             existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
     *             the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
     *             are automatically allowed.</p>
     */
    public readonly alternateDataSourceParameters!: pulumi.Output<outputs.quicksight.DataSourceParameters[] | undefined>;
    /**
     * <p>The Amazon Resource Name (ARN) of the data source.</p>
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly awsAccountId!: pulumi.Output<string | undefined>;
    /**
     * <p>The time that this data source was created.</p>
     */
    public /*out*/ readonly createdTime!: pulumi.Output<string>;
    public readonly credentials!: pulumi.Output<outputs.quicksight.DataSourceCredentials | undefined>;
    public readonly dataSourceId!: pulumi.Output<string | undefined>;
    public readonly dataSourceParameters!: pulumi.Output<outputs.quicksight.DataSourceParameters | undefined>;
    public readonly errorInfo!: pulumi.Output<outputs.quicksight.DataSourceErrorInfo | undefined>;
    /**
     * <p>The last time that this data source was updated.</p>
     */
    public /*out*/ readonly lastUpdatedTime!: pulumi.Output<string>;
    /**
     * <p>A display name for the data source.</p>
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * <p>A list of resource permissions on the data source.</p>
     */
    public readonly permissions!: pulumi.Output<outputs.quicksight.DataSourceResourcePermission[] | undefined>;
    public readonly sslProperties!: pulumi.Output<outputs.quicksight.DataSourceSslProperties | undefined>;
    public /*out*/ readonly status!: pulumi.Output<enums.quicksight.DataSourceResourceStatus>;
    /**
     * <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
     */
    public readonly tags!: pulumi.Output<outputs.quicksight.DataSourceTag[] | undefined>;
    public readonly type!: pulumi.Output<enums.quicksight.DataSourceType | undefined>;
    public readonly vpcConnectionProperties!: pulumi.Output<outputs.quicksight.DataSourceVpcConnectionProperties | undefined>;

    /**
     * Create a DataSource resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DataSourceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["alternateDataSourceParameters"] = args ? args.alternateDataSourceParameters : undefined;
            resourceInputs["awsAccountId"] = args ? args.awsAccountId : undefined;
            resourceInputs["credentials"] = args ? args.credentials : undefined;
            resourceInputs["dataSourceId"] = args ? args.dataSourceId : undefined;
            resourceInputs["dataSourceParameters"] = args ? args.dataSourceParameters : undefined;
            resourceInputs["errorInfo"] = args ? args.errorInfo : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["permissions"] = args ? args.permissions : undefined;
            resourceInputs["sslProperties"] = args ? args.sslProperties : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["vpcConnectionProperties"] = args ? args.vpcConnectionProperties : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["createdTime"] = undefined /*out*/;
            resourceInputs["lastUpdatedTime"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        } else {
            resourceInputs["alternateDataSourceParameters"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["awsAccountId"] = undefined /*out*/;
            resourceInputs["createdTime"] = undefined /*out*/;
            resourceInputs["credentials"] = undefined /*out*/;
            resourceInputs["dataSourceId"] = undefined /*out*/;
            resourceInputs["dataSourceParameters"] = undefined /*out*/;
            resourceInputs["errorInfo"] = undefined /*out*/;
            resourceInputs["lastUpdatedTime"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["permissions"] = undefined /*out*/;
            resourceInputs["sslProperties"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["vpcConnectionProperties"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DataSource.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DataSource resource.
 */
export interface DataSourceArgs {
    /**
     * <p>A set of alternate data source parameters that you want to share for the credentials
     *             stored with this data source. The credentials are applied in tandem with the data source
     *             parameters when you copy a data source by using a create or update request. The API
     *             operation compares the <code>DataSourceParameters</code> structure that's in the request
     *             with the structures in the <code>AlternateDataSourceParameters</code> allow list. If the
     *             structures are an exact match, the request is allowed to use the credentials from this
     *             existing data source. If the <code>AlternateDataSourceParameters</code> list is null,
     *             the <code>Credentials</code> originally used with this <code>DataSourceParameters</code>
     *             are automatically allowed.</p>
     */
    alternateDataSourceParameters?: pulumi.Input<pulumi.Input<inputs.quicksight.DataSourceParametersArgs>[]>;
    awsAccountId?: pulumi.Input<string>;
    credentials?: pulumi.Input<inputs.quicksight.DataSourceCredentialsArgs>;
    dataSourceId?: pulumi.Input<string>;
    dataSourceParameters?: pulumi.Input<inputs.quicksight.DataSourceParametersArgs>;
    errorInfo?: pulumi.Input<inputs.quicksight.DataSourceErrorInfoArgs>;
    /**
     * <p>A display name for the data source.</p>
     */
    name?: pulumi.Input<string>;
    /**
     * <p>A list of resource permissions on the data source.</p>
     */
    permissions?: pulumi.Input<pulumi.Input<inputs.quicksight.DataSourceResourcePermissionArgs>[]>;
    sslProperties?: pulumi.Input<inputs.quicksight.DataSourceSslPropertiesArgs>;
    /**
     * <p>Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.</p>
     */
    tags?: pulumi.Input<pulumi.Input<inputs.quicksight.DataSourceTagArgs>[]>;
    type?: pulumi.Input<enums.quicksight.DataSourceType>;
    vpcConnectionProperties?: pulumi.Input<inputs.quicksight.DataSourceVpcConnectionPropertiesArgs>;
}
