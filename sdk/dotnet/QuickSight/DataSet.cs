// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html
    /// </summary>
    [AwsNativeResourceType("aws-native:quicksight:DataSet")]
    public partial class DataSet : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-awsaccountid
        /// </summary>
        [Output("awsAccountId")]
        public Output<string?> AwsAccountId { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columngroups
        /// </summary>
        [Output("columnGroups")]
        public Output<ImmutableArray<Outputs.DataSetColumnGroup>> ColumnGroups { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columnlevelpermissionrules
        /// </summary>
        [Output("columnLevelPermissionRules")]
        public Output<ImmutableArray<Outputs.DataSetColumnLevelPermissionRule>> ColumnLevelPermissionRules { get; private set; } = null!;

        [Output("consumedSpiceCapacityInBytes")]
        public Output<double> ConsumedSpiceCapacityInBytes { get; private set; } = null!;

        [Output("createdTime")]
        public Output<string> CreatedTime { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-datasetid
        /// </summary>
        [Output("dataSetId")]
        public Output<string?> DataSetId { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-fieldfolders
        /// </summary>
        [Output("fieldFolders")]
        public Output<ImmutableDictionary<string, Outputs.DataSetFieldFolder>?> FieldFolders { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-importmode
        /// </summary>
        [Output("importMode")]
        public Output<string?> ImportMode { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-ingestionwaitpolicy
        /// </summary>
        [Output("ingestionWaitPolicy")]
        public Output<Outputs.DataSetIngestionWaitPolicy?> IngestionWaitPolicy { get; private set; } = null!;

        [Output("lastUpdatedTime")]
        public Output<string> LastUpdatedTime { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-logicaltablemap
        /// </summary>
        [Output("logicalTableMap")]
        public Output<ImmutableDictionary<string, Outputs.DataSetLogicalTable>?> LogicalTableMap { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-name
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("outputColumns")]
        public Output<ImmutableArray<Outputs.DataSetOutputColumn>> OutputColumns { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-permissions
        /// </summary>
        [Output("permissions")]
        public Output<ImmutableArray<Outputs.DataSetResourcePermission>> Permissions { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-physicaltablemap
        /// </summary>
        [Output("physicalTableMap")]
        public Output<ImmutableDictionary<string, Outputs.DataSetPhysicalTable>?> PhysicalTableMap { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset
        /// </summary>
        [Output("rowLevelPermissionDataSet")]
        public Output<Outputs.DataSetRowLevelPermissionDataSet?> RowLevelPermissionDataSet { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DataSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSet(string name, DataSetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:DataSet", name, args ?? new DataSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:quicksight:DataSet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DataSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataSet(name, id, options);
        }
    }

    public sealed class DataSetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-awsaccountid
        /// </summary>
        [Input("awsAccountId")]
        public Input<string>? AwsAccountId { get; set; }

        [Input("columnGroups")]
        private InputList<Inputs.DataSetColumnGroupArgs>? _columnGroups;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columngroups
        /// </summary>
        public InputList<Inputs.DataSetColumnGroupArgs> ColumnGroups
        {
            get => _columnGroups ?? (_columnGroups = new InputList<Inputs.DataSetColumnGroupArgs>());
            set => _columnGroups = value;
        }

        [Input("columnLevelPermissionRules")]
        private InputList<Inputs.DataSetColumnLevelPermissionRuleArgs>? _columnLevelPermissionRules;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-columnlevelpermissionrules
        /// </summary>
        public InputList<Inputs.DataSetColumnLevelPermissionRuleArgs> ColumnLevelPermissionRules
        {
            get => _columnLevelPermissionRules ?? (_columnLevelPermissionRules = new InputList<Inputs.DataSetColumnLevelPermissionRuleArgs>());
            set => _columnLevelPermissionRules = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-datasetid
        /// </summary>
        [Input("dataSetId")]
        public Input<string>? DataSetId { get; set; }

        [Input("fieldFolders")]
        private InputMap<Inputs.DataSetFieldFolderArgs>? _fieldFolders;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-fieldfolders
        /// </summary>
        public InputMap<Inputs.DataSetFieldFolderArgs> FieldFolders
        {
            get => _fieldFolders ?? (_fieldFolders = new InputMap<Inputs.DataSetFieldFolderArgs>());
            set => _fieldFolders = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-importmode
        /// </summary>
        [Input("importMode")]
        public Input<string>? ImportMode { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-ingestionwaitpolicy
        /// </summary>
        [Input("ingestionWaitPolicy")]
        public Input<Inputs.DataSetIngestionWaitPolicyArgs>? IngestionWaitPolicy { get; set; }

        [Input("logicalTableMap")]
        private InputMap<Inputs.DataSetLogicalTableArgs>? _logicalTableMap;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-logicaltablemap
        /// </summary>
        public InputMap<Inputs.DataSetLogicalTableArgs> LogicalTableMap
        {
            get => _logicalTableMap ?? (_logicalTableMap = new InputMap<Inputs.DataSetLogicalTableArgs>());
            set => _logicalTableMap = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("permissions")]
        private InputList<Inputs.DataSetResourcePermissionArgs>? _permissions;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-permissions
        /// </summary>
        public InputList<Inputs.DataSetResourcePermissionArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.DataSetResourcePermissionArgs>());
            set => _permissions = value;
        }

        [Input("physicalTableMap")]
        private InputMap<Inputs.DataSetPhysicalTableArgs>? _physicalTableMap;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-physicaltablemap
        /// </summary>
        public InputMap<Inputs.DataSetPhysicalTableArgs> PhysicalTableMap
        {
            get => _physicalTableMap ?? (_physicalTableMap = new InputMap<Inputs.DataSetPhysicalTableArgs>());
            set => _physicalTableMap = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-rowlevelpermissiondataset
        /// </summary>
        [Input("rowLevelPermissionDataSet")]
        public Input<Inputs.DataSetRowLevelPermissionDataSetArgs>? RowLevelPermissionDataSet { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-dataset.html#cfn-quicksight-dataset-tags
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public DataSetArgs()
        {
        }
    }
}
