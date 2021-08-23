// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html
 */
export class DataSet extends pulumi.CustomResource {
    /**
     * Get an existing DataSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DataSet {
        return new DataSet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:quicksight:DataSet';

    /**
     * Returns true if the given object is an instance of DataSet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataSet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataSet.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-awsaccountid
     */
    public readonly awsAccountId!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columngroups
     */
    public readonly columnGroups!: pulumi.Output<outputs.quicksight.DataSetColumnGroup[] | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columnlevelpermissionrules
     */
    public readonly columnLevelPermissionRules!: pulumi.Output<outputs.quicksight.DataSetColumnLevelPermissionRule[] | undefined>;
    public /*out*/ readonly consumedSpiceCapacityInBytes!: pulumi.Output<number>;
    public /*out*/ readonly createdTime!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-datasetid
     */
    public readonly dataSetId!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-fieldfolders
     */
    public readonly fieldFolders!: pulumi.Output<{[key: string]: outputs.quicksight.DataSetFieldFolder} | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-importmode
     */
    public readonly importMode!: pulumi.Output<string | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-ingestionwaitpolicy
     */
    public readonly ingestionWaitPolicy!: pulumi.Output<outputs.quicksight.DataSetIngestionWaitPolicy | undefined>;
    public /*out*/ readonly lastUpdatedTime!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-logicaltablemap
     */
    public readonly logicalTableMap!: pulumi.Output<{[key: string]: outputs.quicksight.DataSetLogicalTable} | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-name
     */
    public readonly name!: pulumi.Output<string | undefined>;
    public /*out*/ readonly outputColumns!: pulumi.Output<outputs.quicksight.DataSetOutputColumn[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-permissions
     */
    public readonly permissions!: pulumi.Output<outputs.quicksight.DataSetResourcePermission[] | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-physicaltablemap
     */
    public readonly physicalTableMap!: pulumi.Output<{[key: string]: outputs.quicksight.DataSetPhysicalTable} | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset
     */
    public readonly rowLevelPermissionDataSet!: pulumi.Output<outputs.quicksight.DataSetRowLevelPermissionDataSet | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-tags
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a DataSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DataSetArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["awsAccountId"] = args ? args.awsAccountId : undefined;
            inputs["columnGroups"] = args ? args.columnGroups : undefined;
            inputs["columnLevelPermissionRules"] = args ? args.columnLevelPermissionRules : undefined;
            inputs["dataSetId"] = args ? args.dataSetId : undefined;
            inputs["fieldFolders"] = args ? args.fieldFolders : undefined;
            inputs["importMode"] = args ? args.importMode : undefined;
            inputs["ingestionWaitPolicy"] = args ? args.ingestionWaitPolicy : undefined;
            inputs["logicalTableMap"] = args ? args.logicalTableMap : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["permissions"] = args ? args.permissions : undefined;
            inputs["physicalTableMap"] = args ? args.physicalTableMap : undefined;
            inputs["rowLevelPermissionDataSet"] = args ? args.rowLevelPermissionDataSet : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["consumedSpiceCapacityInBytes"] = undefined /*out*/;
            inputs["createdTime"] = undefined /*out*/;
            inputs["lastUpdatedTime"] = undefined /*out*/;
            inputs["outputColumns"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["awsAccountId"] = undefined /*out*/;
            inputs["columnGroups"] = undefined /*out*/;
            inputs["columnLevelPermissionRules"] = undefined /*out*/;
            inputs["consumedSpiceCapacityInBytes"] = undefined /*out*/;
            inputs["createdTime"] = undefined /*out*/;
            inputs["dataSetId"] = undefined /*out*/;
            inputs["fieldFolders"] = undefined /*out*/;
            inputs["importMode"] = undefined /*out*/;
            inputs["ingestionWaitPolicy"] = undefined /*out*/;
            inputs["lastUpdatedTime"] = undefined /*out*/;
            inputs["logicalTableMap"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["outputColumns"] = undefined /*out*/;
            inputs["permissions"] = undefined /*out*/;
            inputs["physicalTableMap"] = undefined /*out*/;
            inputs["rowLevelPermissionDataSet"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(DataSet.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a DataSet resource.
 */
export interface DataSetArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-awsaccountid
     */
    awsAccountId?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columngroups
     */
    columnGroups?: pulumi.Input<pulumi.Input<inputs.quicksight.DataSetColumnGroupArgs>[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columnlevelpermissionrules
     */
    columnLevelPermissionRules?: pulumi.Input<pulumi.Input<inputs.quicksight.DataSetColumnLevelPermissionRuleArgs>[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-datasetid
     */
    dataSetId?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-fieldfolders
     */
    fieldFolders?: pulumi.Input<{[key: string]: pulumi.Input<inputs.quicksight.DataSetFieldFolderArgs>}>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-importmode
     */
    importMode?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-ingestionwaitpolicy
     */
    ingestionWaitPolicy?: pulumi.Input<inputs.quicksight.DataSetIngestionWaitPolicyArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-logicaltablemap
     */
    logicalTableMap?: pulumi.Input<{[key: string]: pulumi.Input<inputs.quicksight.DataSetLogicalTableArgs>}>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-name
     */
    name?: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-permissions
     */
    permissions?: pulumi.Input<pulumi.Input<inputs.quicksight.DataSetResourcePermissionArgs>[]>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-physicaltablemap
     */
    physicalTableMap?: pulumi.Input<{[key: string]: pulumi.Input<inputs.quicksight.DataSetPhysicalTableArgs>}>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset
     */
    rowLevelPermissionDataSet?: pulumi.Input<inputs.quicksight.DataSetRowLevelPermissionDataSetArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-tags
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
